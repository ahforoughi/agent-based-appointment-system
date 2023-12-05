import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import User, SessionLocal
from sqlalchemy.orm import Session
from agents.registeration_agent import RegisterationAgent
from agents.client_agent import ClientAgent
from constants import REGISTER_AGENT, CLIENT_AGENT


async def main():
    registeration_agent = RegisterationAgent(REGISTER_AGENT.jid, REGISTER_AGENT.password)
    await registeration_agent.start(auto_register=True)
    print("Receiver started")

    client_agent = ClientAgent(CLIENT_AGENT.jid, CLIENT_AGENT.password)
    await client_agent.start(auto_register=True)
    print("Sender started")

    await spade.wait_until_finished(registeration_agent)
    print("Agents finished")


if __name__ == "__main__":
    spade.run(main())