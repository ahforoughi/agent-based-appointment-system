# constants.py
from dataclasses import dataclass
from enum import Enum



@dataclass
class AgentInfo:
    jid: str
    password: str


REGISTER_AGENT = AgentInfo(jid="register@localhost", password="123")
LOGIN_AGENT = AgentInfo(jid="login@localhost", password="123")
SCHEDULER_AGENT = AgentInfo(jid="scheduler@localhost", password="123")
EMAIL_AGENT = AgentInfo(jid="email@localhost", password="123")
CLIENT_AGENT = AgentInfo(jid="client@localhost", password="123")
