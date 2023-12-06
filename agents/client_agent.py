import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import User, SessionLocal
from sqlalchemy.orm import Session


class ClientAgent(Agent):
    def __init__(self, jid, password, behavior, username, email=None, phone=None, user_password=None):
        print("ClientAgent init")
        super().__init__(jid, password)

        self.behavior = behavior
        self.username = username
        self.email = email
        self.phone = phone
        self.user_password = user_password
    

    
    class RegisterationBehavior(OneShotBehaviour):
        async def run(self):
            # get the attributes from the ClientAgent class
            self.username = self.agent.username
            self.email = self.agent.email
            self.phone = self.agent.phone
            self.user_password = self.agent.user_password
            
            print("RegisterationBehavior running", )
            msg = Message(to="register@localhost")     # Instantiate the message
            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
            msg.set_metadata("ontology", "myOntology")  # Set the ontology of the message content
            msg.set_metadata("language", "OWL-S")       # Set the language of the message content
            
            msg.body = json.dumps({
            "username": self.username,
            "user_password": self.user_password,
            "email": self.email,
            "phone": self.phone
            })                    

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()

    class LoginBehavior(OneShotBehaviour):
        async def run(self):
            print("LoginBehavior running")
            
            self.username = self.agent.username
            self.user_password = self.agent.user_password

            msg = Message(to="login@localhost")     # Instantiate the message
            # msg.set_metadata("performative", "Request")  # Set the "inform" FIPA performative
            
            
            msg.body = json.dumps({
            "username": self.username,
            "user_password": self.user_password,

            })                    

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()


    class GetAppoinmentsTimesBehavior(OneShotBehaviour):
        async def run(self):
            print("GetAppoinmentsTimesBehavior running")

    
    
    async def setup(self):
        print("ClientAgent started")
        
        if self.behavior == "login":
            self.login_behavior = self.LoginBehavior()
            self.add_behaviour(self.login_behavior)
        elif self.behavior == "get_appoinments_times":
            self.get_appoinments_times_behavior = self.GetAppoinmentsTimesBehavior()
            self.add_behaviour(self.get_appoinments_times_behavior)
        elif self.behavior == "register"    :   
            self.registeration_behavior = self.RegisterationBehavior()
            self.add_behaviour(self.registeration_behavior)





