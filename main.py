import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import User, SessionLocal
from sqlalchemy.orm import Session
from agents.registeration_agent import RegisterationAgent
from agents.scheduler_agent import SchedulerAgent
from agents.client_agent import ClientAgent
from constants import REGISTER_AGENT, CLIENT_AGENT, SCHEDULER_AGENT

# take command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--register", help="register new user", nargs='*')
parser.add_argument("--login", help="login user", action="store_true")
parser.add_argument("--get_appoinments_times", help="get appoinments times", action="store_true")
parser.add_argument("--set_appoinment", help="set appoinment", action="store_true")

args = parser.parse_args()

# define a variable to set the action of the agent based on the command line arguments
behavior = None
if args.register not in [False, True]:
    print(f"Registering new user with identifier: {args.register}")
    behavior = "register"
elif args.login:
    behavior = "login"
elif args.get_appoinments_times:
    behavior = "get_appoinments_times"
elif args.set_appoinment:
    behavior = "set_appoinment"

async def main():

    global username, email, phone, user_password
    if args.register:
        print("Registering new user")
        username = args.register[0]
        email = args.register[1]
        phone = args.register[2]
        user_password = args.register[3]

        registeration_agent = RegisterationAgent(REGISTER_AGENT.jid, REGISTER_AGENT.password)
        await registeration_agent.start(auto_register=True)
        print("registeration_agent started")

    print(username, email, phone, user_password)
    client_agent = ClientAgent(CLIENT_AGENT.jid, CLIENT_AGENT.password, behavior=behavior,
                               username=username, email=email, phone=phone, user_password=user_password)
    await client_agent.start(auto_register=True)

    # await spade.wait_until_finished(registeration_agent)
    # print("Agents finished")


if __name__ == "__main__":
    spade.run(main())