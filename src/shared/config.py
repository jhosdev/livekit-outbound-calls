from dataclasses import dataclass
from typing import Literal

from attrs import define
from livekit.agents import Agent


@define
class AgentSession:
    llm: str
    stt: str
    tts: str
    stt_language: Literal["multi", "es", "en"] = "multi"


AgentList = Literal["greeter", "main"]


@dataclass
class SessionInfo:
    agents: dict[AgentList, Agent]
    prev_agent: Agent | None = None
    customer_name: str | None = None
    customer_phone: str | None = None
