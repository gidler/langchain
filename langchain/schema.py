from __future__ import annotations

from typing import NamedTuple


class AgentAction(NamedTuple):
    """Agent's action to take."""

    tool: str
    tool_input: str
    log: str