import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import User, SessionLocal
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class RegisterationAgent(Agent):
    class RecvBehav(OneShotBehaviour):
        async def run(self):
            print("RegisterationAgent RecvBehav running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            try:
                data = json.loads(msg.body)

                username = data["username"]
                password = data["password"]
                email = data["email"]
                phone = data["phone"]

                db: Session = SessionLocal()

                # Check if user exists
                if db.query(User).filter(User.username == username).first():
                    print(f"User {username} already exists.")
                else:
                    # Register new user
                    new_user = User(username=username, password=password)
                    db.add(new_user)
                    db.commit()
                    print(f"Registered new user: {username}")

                db.close()
            except Exception as e:
                print(f"An error occurred: {e}")

            # stop agent from behaviour
            await self.agent.stop()

    async def setup(self):
        print("RegisterationAgent started")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)
