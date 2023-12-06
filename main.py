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

# take command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--register", help="register new user", action="store_true")
parser.add_argument("--login", help="login user", action="store_true")
parser.add_argument("--get_appoinments_times", help="get appoinments times", action="store_true")

args = parser.parse_args()

if args.register:
    print("Registering new user")

# define a variable to set the action of the agent based on the command line arguments
behavior = None
if args.register:
    behavior = "register"
elif args.login:
    behavior = "login"
elif args.get_appoinments_times:
    behavior = "get_appoinments_times"

async def main():
    registeration_agent = RegisterationAgent(REGISTER_AGENT.jid, REGISTER_AGENT.password)
    await registeration_agent.start(auto_register=True)
    print("Receiver started")

    client_agent = ClientAgent(CLIENT_AGENT.jid, CLIENT_AGENT.password, behavior=behavior)
    await client_agent.start(auto_register=True)
    print("Sender started")

    # await spade.wait_until_finished(registeration_agent)
    # print("Agents finished")


if __name__ == "__main__":
    spade.run(main())