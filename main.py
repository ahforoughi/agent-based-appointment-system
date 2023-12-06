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
from agents.login_agent import LoginAgent
from constants import REGISTER_AGENT, CLIENT_AGENT, LOGIN_AGENT

from args_parser import parser

args = parser.parse_args()



def get_behavior():
    if args.register:
        return "register"
    elif args.login:
        return "login"
    elif args.get_appoinments_times:
        return "get_appoinments_times"

behavior = get_behavior()

print(f"Behavior: {behavior}")

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

        client_agent = ClientAgent(CLIENT_AGENT.jid, CLIENT_AGENT.password, behavior=behavior,
                                username=username, email=email, phone=phone, user_password=user_password)
        await client_agent.start(auto_register=True)
        print(f"Client Agent with behavior {behavior} started")



    elif args.login:
        username = args.login[0]
        user_password = args.login[1]
        
        login_agent = LoginAgent(LOGIN_AGENT.jid, LOGIN_AGENT.password)
        await login_agent.start(auto_register=True)

        client_agent = ClientAgent(CLIENT_AGENT.jid, CLIENT_AGENT.password, behavior=behavior,
                                username=username, user_password=user_password)
        await client_agent.start(auto_register=True)
        print(f"Client Agent with behavior {behavior} started")
    







    # await spade.wait_until_finished(ClientAgent)
    # print("Agents finished")


if __name__ == "__main__":
    spade.run(main())