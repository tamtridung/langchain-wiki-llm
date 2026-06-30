"""
langchain_utils.py — Utility functions để extract thông tin từ agent messages.

Module này chứa các hàm helper giúp bạn trích xuất thông tin có ý nghĩa từ
message history của LangChain / LangGraph agent (AIMessage, ToolMessage, HumanMessage...).

Các chức năng chính:
  - Phân loại message type
  - Extract plan (write_todos) từ agent messages
  - Extract tool calls và kết quả trả về
  - Extract AI text response
  - Extract interrupt info từ HIL
  - Pretty-print ra console hoặc trả về dict structured
  - Dedup tool calls bằng ID
  - Summarize toàn bộ conversation

Usage:
    from langchain_utils import (
        extract_plans,
        extract_tool_calls,
        extract_tool_results,
        extract_ai_text,
        extract_interrupts,
        summarize_conversation,
        print_messages,
        MessageClassifier,
    )
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

# ──────────────────────────────────────────────
#  Dataclasses cho structured output
# ──────────────────────────────────────────────


@dataclass
class TodoItem:
    """Một task trong plan."""
    content: str
    status: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def display_label(self) -> str:
        return self.title or self.description or self.content


@dataclass
class PlanInfo:
    """Thông tin về một lần gọi write_todos."""
    tool_call_id: str
    todos: list[TodoItem] = field(default_factory=list)
    raw_args: dict = field(default_factory=dict)

    @property
    def total(self) -> int:
        return len(self.todos)

    @property
    def completed(self) -> int:
        return sum(1 for t in self.todos if t.status == "completed")

    @property
    def in_progress(self) -> int:
        return sum(1 for t in self.todos if t.status == "in_progress")


@dataclass
class ToolCallInfo:
    """Thông tin về một tool call."""
    tool_call_id: str
    name: str
    args: dict
    is_plan: bool = False          # write_todos
    plan_detail: Optional[PlanInfo] = None


@dataclass
class ToolResultInfo:
    """Thông tin về kết quả tool execution."""
    tool_call_id: str
    name: str
    content: str
    is_error: bool = False


@dataclass
class AiTextInfo:
    """AI text response (không kèm tool call)."""
    content: str
    message_id: str


@dataclass
class InterruptActionRequest:
    """Một tool call đang chờ HIL duyệt."""
    name: str
    args: dict
    tool_call_id: str


@dataclass
class InterruptInfo:
    """Thông tin về một HIL interrupt."""
    action_requests: list[InterruptActionRequest]
    allowed_decisions: list[str]
    review_configs: list[dict]


@dataclass
class ConversationSummary:
    """Tóm tắt toàn bộ conversation."""
    total_messages: int = 0
    plans: list[PlanInfo] = field(default_factory=list)
    tool_calls: list[ToolCallInfo] = field(default_factory=list)
    tool_results: list[ToolResultInfo] = field(default_factory=list)
    ai_texts: list[AiTextInfo] = field(default_factory=list)
    human_texts: list[str] = field(default_factory=list)
    interrupts: list[InterruptInfo] = field(default_factory=list)


# ──────────────────────────────────────────────
#  Core extraction functions
# ──────────────────────────────────────────────


class MessageClassifier:
    """Phân loại message type."""

    @staticmethod
    def is_ai_message(msg: Any) -> bool:
        return hasattr(msg, "type") and getattr(msg, "type", None) == "ai"

    @staticmethod
    def is_human_message(msg: Any) -> bool:
        return hasattr(msg, "type") and getattr(msg, "type", None) == "human"

    @staticmethod
    def is_tool_message(msg: Any) -> bool:
        return hasattr(msg, "type") and getattr(msg, "type", None) == "tool"

    @staticmethod
    def is_system_message(msg: Any) -> bool:
        return hasattr(msg, "type") and getattr(msg, "type", None) == "system"

    @staticmethod
    def has_tool_calls(msg: Any) -> bool:
        return hasattr(msg, "tool_calls") and bool(msg.tool_calls)

    @staticmethod
    def has_content(msg: Any) -> bool:
        return hasattr(msg, "content") and bool(msg.content)

    @staticmethod
    def classify(msg: Any) -> str:
        """Trả về tên loại message: 'ai', 'human', 'tool', 'system', 'unknown'."""
        if MessageClassifier.is_ai_message(msg):
            return "ai"
        if MessageClassifier.is_human_message(msg):
            return "human"
        if MessageClassifier.is_tool_message(msg):
            return "tool"
        if MessageClassifier.is_system_message(msg):
            return "system"
        return "unknown"


def extract_todo_from_tool_call(tc: dict) -> PlanInfo:
    """Extract plan info từ một tool call dictionary của write_todos."""
    plan = PlanInfo(
        tool_call_id=tc.get("id", ""),
        raw_args=tc.get("args", {}),
    )
    todos_raw = tc.get("args", {}).get("todos", [])
    for item in todos_raw:
        plan.todos.append(
            TodoItem(
                content=item.get("content", ""),
                status=item.get("status"),
                title=item.get("title"),
                description=item.get("description"),
            )
        )
    return plan


def extract_tool_call_info(tc: dict) -> ToolCallInfo:
    """Extract tool call info từ một tool call dictionary."""
    info = ToolCallInfo(
        tool_call_id=tc.get("id", ""),
        name=tc.get("name", "unknown"),
        args=tc.get("args", {}),
    )
    if info.name == "write_todos":
        info.is_plan = True
        info.plan_detail = extract_todo_from_tool_call(tc)
    return info


def extract_plans(messages: list[Any]) -> list[PlanInfo]:
    """Extract tất cả các plan (write_todos) từ message history.

    Args:
        messages: List langchain message objects.

    Returns:
        List[PlanInfo] — mỗi lần agent gọi write_todos là một phần tử.
    """
    plans = []
    seen_ids: set[str] = set()

    for msg in messages:
        if not MessageClassifier.has_tool_calls(msg):
            continue
        for tc in msg.tool_calls:
            if tc.get("name") != "write_todos":
                continue
            tc_id = tc.get("id", "")
            if tc_id in seen_ids:
                continue
            seen_ids.add(tc_id)
            plans.append(extract_todo_from_tool_call(tc))

    return plans


def extract_tool_calls(
    messages: list[Any],
    dedup: bool = True,
    include_plans: bool = True,
) -> list[ToolCallInfo]:
    """Extract tất cả các tool call từ message history.

    Args:
        messages: List langchain message objects.
        dedup: Nếu True, loại bỏ tool call trùng lặp (cùng ID).
        include_plans: Nếu True, bao gồm cả write_todos.

    Returns:
        List[ToolCallInfo] — mỗi tool call là một phần tử.
    """
    calls = []
    seen_ids: set[str] = set()

    for msg in messages:
        if not MessageClassifier.has_tool_calls(msg):
            continue
        for tc in msg.tool_calls:
            tc_id = tc.get("id", "")
            if dedup and tc_id in seen_ids:
                continue
            if dedup:
                seen_ids.add(tc_id)
            if not include_plans and tc.get("name") == "write_todos":
                continue
            calls.append(extract_tool_call_info(tc))

    return calls


def extract_tool_results(messages: list[Any]) -> list[ToolResultInfo]:
    """Extract kết quả trả về của tool execution.

    Args:
        messages: List langchain message objects.

    Returns:
        List[ToolResultInfo] — mỗi tool result là một phần tử.
    """
    results = []

    for msg in messages:
        if not MessageClassifier.is_tool_message(msg):
            continue
        content = msg.content if isinstance(msg.content, str) else str(msg.content)

        # Detect lỗi
        is_error = False
        if isinstance(content, str):
            try:
                parsed = json.loads(content)
                if isinstance(parsed, dict) and "error" in parsed:
                    is_error = True
            except (json.JSONDecodeError, TypeError):
                pass

        results.append(
            ToolResultInfo(
                tool_call_id=getattr(msg, "tool_call_id", ""),
                name=getattr(msg, "name", ""),
                content=content,
                is_error=is_error,
            )
        )

    return results


def extract_ai_text(
    messages: list[Any],
    skip_empty: bool = True,
    skip_tool_call_messages: bool = True,
) -> list[AiTextInfo]:
    """Extract AI text response (không kèm tool call) từ message history.

    Args:
        messages: List langchain message objects.
        skip_empty: Bỏ qua message content rỗng.
        skip_tool_call_messages: Bỏ qua message chỉ chứa tool call.

    Returns:
        List[AiTextInfo] — mỗi AI text response là một phần tử.
    """
    texts: list[AiTextInfo] = []

    for msg in messages:
        if not MessageClassifier.is_ai_message(msg):
            continue
        if skip_empty and not msg.content:
            continue
        if skip_tool_call_messages and MessageClassifier.has_tool_calls(msg):
            continue

        texts.append(
            AiTextInfo(
                content=str(msg.content),
                message_id=getattr(msg, "id", ""),
            )
        )

    return texts


def extract_interrupts(state_data: dict) -> list[InterruptInfo]:
    """Extract thông tin HIL interrupt từ agent state.

    Args:
        state_data: State dict, thường lấy từ agent.get_state(config)
                    hoặc result.interrupts (nếu là list).

    Returns:
        List[InterruptInfo] — các interrupt đang chờ xử lý.
    """
    # Nếu là list (result.interrupts)
    if isinstance(state_data, (list, tuple)):
        raw_interrupts = state_data
    else:
        raw_interrupts = state_data.get("interrupts", [])

    result: list[InterruptInfo] = []
    for interrupt in raw_interrupts:
        if hasattr(interrupt, "value"):
            value = interrupt.value
        else:
            value = interrupt

        action_requests_raw = value.get("action_requests", [])
        review_configs_raw = value.get("review_configs", [])

        action_requests = [
            InterruptActionRequest(
                name=ar["name"],
                args=ar.get("args", {}),
                tool_call_id=ar.get("id", ""),
            )
            for ar in action_requests_raw
        ]

        allowed_decisions = []
        for cfg in review_configs_raw:
            ad = cfg.get("allowed_decisions", [])
            allowed_decisions.extend(ad)

        result.append(
            InterruptInfo(
                action_requests=action_requests,
                allowed_decisions=list(set(allowed_decisions)),
                review_configs=review_configs_raw,
            )
        )

    return result


def extract_human_text(messages: list[Any]) -> list[str]:
    """Extract tất cả user input từ message history."""
    texts = []
    for msg in messages:
        if MessageClassifier.is_human_message(msg) and msg.content:
            texts.append(str(msg.content))
    return texts


# ──────────────────────────────────────────────
#  Summarize & Format
# ──────────────────────────────────────────────


def summarize_conversation(
    messages: list[Any],
    include_human: bool = True,
) -> ConversationSummary:
    """Tóm tắt toàn bộ conversation thành structured data.

    Args:
        messages: List langchain message objects.
        include_human: Có bao gồm human messages không.

    Returns:
        ConversationSummary — dataclass chứa tất cả thông tin.
    """
    summary = ConversationSummary()
    summary.total_messages = len(messages)

    # AI text responses
    summary.ai_texts = extract_ai_text(messages)

    # Plans & tool calls
    for tc in extract_tool_calls(messages, dedup=True, include_plans=True):
        summary.tool_calls.append(tc)
        if tc.is_plan and tc.plan_detail:
            summary.plans.append(tc.plan_detail)

    # Tool results
    summary.tool_results = extract_tool_results(messages)

    # Human messages
    if include_human:
        summary.human_texts = extract_human_text(messages)

    return summary


def format_conversation_summary(summary: ConversationSummary) -> str:
    """Format ConversationSummary thành string để in ra/hiển thị.

    Args:
        summary: ConversationSummary object.

    Returns:
        str — bản text có cấu trúc.
    """
    lines: list[str] = []
    lines.append(f"📊 Conversation Summary ({summary.total_messages} messages)")
    lines.append("=" * 60)

    # Plans
    if summary.plans:
        lines.append(f"\n📋 Plans ({len(summary.plans)} lần write_todos):")
        for i, plan in enumerate(summary.plans, 1):
            lines.append(f"  #{i}: {plan.total} tasks [{plan.completed} completed, {plan.in_progress} in-progress]")
            for j, todo in enumerate(plan.todos, 1):
                status_icon = {
                    "completed": "✅",
                    "in_progress": "🔄",
                    "pending": "⏳",
                }.get(todo.status or "pending", "⏳")
                lines.append(f"     {status_icon} {j}. {todo.display_label()}")

    # Tool calls (excluding plans)
    non_plan_calls = [tc for tc in summary.tool_calls if not tc.is_plan]
    if non_plan_calls:
        lines.append(f"\n🔧 Tool Calls ({len(non_plan_calls)}):")
        for tc in non_plan_calls:
            args_str = json.dumps(tc.args, ensure_ascii=False)
            lines.append(f"  → {tc.name}({args_str})")

    # Tool results
    if summary.tool_results:
        lines.append(f"\n✅ Tool Results ({len(summary.tool_results)}):")
        for tr in summary.tool_results:
            icon = "❌" if tr.is_error else "✅"
            content_preview = tr.content[:150] + "..." if len(tr.content) > 150 else tr.content
            lines.append(f"  {icon} {tr.name}: {content_preview}")

    # AI texts
    if summary.ai_texts:
        lines.append(f"\n🤖 AI Responses ({len(summary.ai_texts)}):")
        for ai in summary.ai_texts:
            preview = ai.content[:200].replace("\n", " ").strip()
            if len(ai.content) > 200:
                preview += "..."
            lines.append(f"  {preview}")

    # Human texts
    if summary.human_texts:
        lines.append(f"\n👤 User Messages ({len(summary.human_texts)}):")
        for h in summary.human_texts:
            preview = h[:200].replace("\n", " ").strip()
            if len(h) > 200:
                preview += "..."
            lines.append(f"  {preview}")

    return "\n".join(lines)


def print_messages(
    messages: list[Any],
    seen_tool_ids: Optional[set[str]] = None,
    logger: Optional[Any] = None,
) -> set[str]:
    """In messages ra console với emoji và định dạng dễ đọc.

    Args:
        messages: List langchain message objects.
        seen_tool_ids: Set chứa các tool call ID đã in (để dedup).
                       Nếu None, tạo mới.
        logger: Nếu có, dùng logger.info() thay vì print().

    Returns:
        set[str] — seen_tool_ids đã được cập nhật (để dùng cho lần gọi sau).
    """
    if seen_tool_ids is None:
        seen_tool_ids = set()

    for msg in messages:
        # ── Tool calls ──
        if MessageClassifier.has_tool_calls(msg):
            for tc in msg.tool_calls:
                tc_id = tc.get("id", "")
                if tc_id in seen_tool_ids:
                    continue
                seen_tool_ids.add(tc_id)

                if tc["name"] == "write_todos":
                    todos = tc["args"].get("todos", [])
                    _log_or_print(f"\n  📋 PLAN — {len(todos)} task(s):", logger)
                    for i, t in enumerate(todos, 1):
                        label = t.get("title") or t.get("description") or t.get("content", "?")
                        _log_or_print(f"       {i}. {label}", logger)
                else:
                    args_str = json.dumps(tc["args"], ensure_ascii=False)
                    _log_or_print(f"\n  🔧 → {tc['name']}({args_str})", logger)

        # ── Tool results ──
        if MessageClassifier.is_tool_message(msg):
            content = msg.content if isinstance(msg.content, str) else str(msg.content)[:500]
            _log_or_print(f"     ✅ Result: {content}", logger)

        # ── AI text response ──
        if (
            MessageClassifier.is_ai_message(msg)
            and msg.content
            and not MessageClassifier.has_tool_calls(msg)
        ):
            _log_or_print(f"\n  🤖 {msg.content[:]}", logger)

    return seen_tool_ids


def _log_or_print(text: str, logger: Optional[Any] = None) -> None:
    """In text ra console hoặc dùng logger."""
    if logger:
        logger.info(text)
    else:
        print(text, flush=True)


# ──────────────────────────────────────────────
#  High-level helpers
# ──────────────────────────────────────────────


def get_latest_plan(plans: list[PlanInfo]) -> Optional[PlanInfo]:
    """Lấy plan mới nhất (cuối cùng) từ danh sách plan."""
    return plans[-1] if plans else None


def get_plan_progress(plan: PlanInfo) -> str:
    """Trả về progress bar text của plan.

    Ví dụ: "3/6 tasks completed (🟢🟢🟢🟡⚪⚪)"
    """
    if not plan.todos:
        return "No tasks"
    done = plan.completed
    total = plan.total
    blocks = []
    for todo in plan.todos:
        if todo.status == "completed":
            blocks.append("🟢")
        elif todo.status == "in_progress":
            blocks.append("🟡")
        else:
            blocks.append("⚪")
    bar = "".join(blocks)
    return f"{done}/{total} tasks ({bar})"


def find_plan_by_content(plans: list[PlanInfo], keyword: str) -> list[PlanInfo]:
    """Tìm plan có chứa keyword trong task content."""
    keyword_lower = keyword.lower()
    matches = []
    for plan in plans:
        for todo in plan.todos:
            if keyword_lower in todo.content.lower():
                matches.append(plan)
                break
    return matches


def messages_to_json(messages: list[Any]) -> str:
    """Chuyển messages thành JSON string để debug/storage.

    Args:
        messages: List langchain message objects.

    Returns:
        str — JSON string với các trường chính.
    """
    result: list[dict] = []
    for msg in messages:
        entry: dict[str, Any] = {
            "type": MessageClassifier.classify(msg),
        }
        if hasattr(msg, "content") and msg.content:
            entry["content"] = str(msg.content)[:1000]
        if MessageClassifier.has_tool_calls(msg):
            entry["tool_calls"] = [
                {
                    "name": tc["name"],
                    "args": tc.get("args", {}),
                    "id": tc.get("id", ""),
                }
                for tc in msg.tool_calls
            ]
        if MessageClassifier.is_tool_message(msg):
            entry["name"] = getattr(msg, "name", "")
            entry["tool_call_id"] = getattr(msg, "tool_call_id", "")
        result.append(entry)
    return json.dumps(result, ensure_ascii=False, indent=2)


# ──────────────────────────────────────────────
#  Interrupt helpers
# ──────────────────────────────────────────────


def format_interrupt_request(action: InterruptActionRequest, index: int = 1) -> str:
    """Format một action request để hiển thị cho user."""
    args_str = json.dumps(action.args, ensure_ascii=False, indent=2)
    return (
        f"  #{index} 🔧 {action.name}\n"
        f"     Args: {args_str}"
    )


def build_approve_decisions(action_requests: list[InterruptActionRequest]) -> list[dict]:
    """Tạo decisions list để approve tất cả action requests."""
    return [{"type": "approve"} for _ in action_requests]


def build_reject_decisions(
    action_requests: list[InterruptActionRequest],
    message: str = "User rejected this operation.",
) -> list[dict]:
    """Tạo decisions list để reject tất cả action requests."""
    return [{"type": "reject", "message": message} for _ in action_requests]


def build_edit_decisions(
    action_requests: list[InterruptActionRequest],
    edits: list[dict[str, Any]],
) -> list[dict]:
    """Tạo decisions list với edit cho từng action request.

    Args:
        action_requests: Danh sách action requests gốc.
        edits: List dict, mỗi dict chứa args mới.
               Ví dụ: [{"type": "edit", "edited_action": {"name": "send_email", "args": {"to": "new@example.com"}}}]

    Returns:
        List[dict] — decisions list.
    """
    decisions = []
    for i, action in enumerate(action_requests):
        if i < len(edits) and edits[i].get("type") == "edit":
            decisions.append(edits[i])
        else:
            decisions.append({"type": "approve"})
    return decisions


# ──────────────────────────────────────────────
#  Agent result extraction (result.value pattern)
# ──────────────────────────────────────────────


def extract_from_result(result: Any) -> ConversationSummary:
    """Extract thông tin từ agent.invoke() result object.

    Thường dùng với result.value['messages'] pattern của Deep Agents SDK.

    Args:
        result: Kết quả từ agent.invoke() hoặc agent.stream()

    Returns:
        ConversationSummary
    """
    # result.value chứa state
    if hasattr(result, "value"):
        value = result.value
    elif isinstance(result, dict):
        value = result
    else:
        value = {}

    # Lấy messages từ nhiều format khác nhau
    messages = None
    if isinstance(value, dict):
        messages = value.get("messages")
    if messages is None and hasattr(value, "get"):
        messages = value.get("data", {}).get("messages")

    if not messages:
        return ConversationSummary()

    return summarize_conversation(messages)


def get_messages_from_state(state: Any) -> list[Any]:
    """Lấy messages từ state object với nhiều format khác nhau.

    Hỗ trợ:
      - state['messages']
      - state['data']['messages']
      - state.value['messages']
      - state.value['data']['messages']
    """
    if isinstance(state, dict):
        if "messages" in state:
            return state["messages"]
        if "data" in state and isinstance(state["data"], dict):
            return state["data"].get("messages", [])
    elif hasattr(state, "value"):
        return get_messages_from_state(state.value)

    return []
