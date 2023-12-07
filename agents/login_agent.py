import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class LoginAgent(Agent):

    class LoginUser(OneShotBehaviour):
        async def run(self):
            print("LoginUser running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            try:
                data = json.loads(msg.body)

                username = data["username"]
                user_password = data["user_password"]

                db: Session = SessionLocal()

                # check for user in database and return user id if exists or None if not exists 
                user = db.query(Patient).filter(Patient.username == username).first()
                if user:
                    if user.user_password == user_password:
                        print(f"User {username} logged in.")
                    else:
                        print(f"User {username} password is incorrect.")
                else:
                    print(f"User {username} does not exist.")

            except Exception as e:
                print(f"An error occurred: {e}")

            # stop agent from behaviour
            await self.agent.stop()

    async def setup(self):
        print("LoginAgent started")
        b = self.LoginUser()
        template = Template()
        # template.set_metadata("performative", "Request")
        self.add_behaviour(b, template)
