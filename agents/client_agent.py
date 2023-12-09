import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
import json


class ClientAgent(Agent):
    def __init__(self, jid, password, behavior, 
                 firstname=None, lastname=None, username=None, phone=None, user_password=None, 
                 appoinment_type=None, appoinment_id=None):
        print("ClientAgent init")
        super().__init__(jid, password)

        self.behavior = behavior
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone = phone
        self.user_password = user_password
        self.appoinment_type = appoinment_type
        self.appoinment_id = appoinment_id
    

    
    class RegisterationBehavior(OneShotBehaviour):
        async def run(self):
            # get the attributes from the ClientAgent class
            self.firstname = self.agent.firstname
            self.lastname = self.agent.lastname
            self.username = self.agent.username
            self.phone = self.agent.phone
            self.user_password = self.agent.user_password
            
            print("RegisterationBehavior in Client Agent running", )
            msg = Message(to="register@localhost")     # Instantiate the message
            # msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
            msg.set_metadata("ontology", "myOntology")  # Set the ontology of the message content
            msg.set_metadata("language", "OWL-S")       # Set the language of the message content
            
            msg.body = json.dumps({
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "user_password": self.user_password,
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
            print("LoginBehavior in Client Agent running")
            
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
            print("GetAppoinmentsTimesBehavior in Client Agent running")
            msg = Message(to="scheduler@localhost")     # Instantiate the message
            msg.set_metadata("performative", "request")  # Set the "inform" FIPA performative
            # msg.set_metadata("action", "get_appoinments_times")  
            
            msg.body = json.dumps({
            "appoinment_type": self.agent.appoinment_type
            })                    

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()
            

    class SetAppoinmentBehavior(OneShotBehaviour):
        async def run(self):
            print("SetAppoinmentBehavior in Client Agent running")
            
            msg = Message(to="scheduler@localhost")     # Instantiate the message
            msg.set_metadata("performative", "request")  # Set the "inform" FIPA performative

            msg.body = json.dumps({
            "appoinment_id": self.agent.appoinment_id, 
            "username": self.agent.username
            })

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()

    class SendEmailBehavior(OneShotBehaviour):
        async def run(self):
            print("SendEmailBehavior in Client Agent running")
            
            msg = Message(to="email@localhost")     # Instantiate the message
            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
            msg.body = json.dumps({
            "username": self.agent.username
            })

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()


    async def setup(self):
        print("ClientAgent started")
        
        if self.behavior == "login":
            self.login_behavior = self.LoginBehavior()
            self.add_behaviour(self.login_behavior)
        elif self.behavior == "get_appoinments_times":
            self.get_appoinments_times_behavior = self.GetAppoinmentsTimesBehavior()
            self.add_behaviour(self.get_appoinments_times_behavior)
        elif self.behavior == "set_appoinment":
            self.set_appoinment_behavior = self.SetAppoinmentBehavior()
            self.add_behaviour(self.set_appoinment_behavior)
        elif self.behavior == "register":   
            self.registeration_behavior = self.RegisterationBehavior()
            self.add_behaviour(self.registeration_behavior)
        elif self.behavior == "send_email":
            self.send_email_behavior = self.SendEmailBehavior()
            self.add_behaviour(self.send_email_behavior)



