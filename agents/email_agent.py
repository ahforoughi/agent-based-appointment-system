import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class EmailAgent(Agent):

    class SendEmail(OneShotBehaviour):
        async def run(self):
            print("SendEmail running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")


    async def setup(self):
        print("EmailAgent started")
        b = self.SendEmail()
        template = Template()
        # template.set_metadata("performative", "Request")
        self.add_behaviour(b, template)
