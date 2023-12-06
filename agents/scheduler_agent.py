from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import User, SessionLocal
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class SchedulerAgent(Agent):
    class ReturnAvailableTimes(CyclicBehaviour):
        async def run(self):
            print("ReturnAvailableTimes running")
    
  



    class SetAppoinment(CyclicBehaviour):
        async def run(self):
            print("SetAppoinment running")

            msg = await self.receive(timeout=10)
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            await self.agent.stop()


    
    async def setup(self):
        print("SchedulerAgent started")
        
        print("ReturnAvailableTimes added")
        receive_times_behavior = self.ReturnAvailableTimes()
        receive_times_template = Template()
        receive_times_template.set_metadata("performative", "inform")
        self.add_behaviour(receive_times_behavior, receive_times_template)

        print("SetAppoinment added")
        set_time_behavior = self.SetAppoinment()
        set_time_template = Template()
        set_time_template.set_metadata("performative", "request")
        self.add_behaviour(set_time_behavior, set_time_template)


