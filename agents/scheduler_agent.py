from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal, Appointment, Doctor
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class SchedulerAgent(Agent):
    class ReturnAvailableTimes(OneShotBehaviour):
        async def run(self):
            print("ReturnAvailableTimes running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            try:
                data = json.loads(msg.body)

                appoinment_type = data["appoinment_type"]

                db: Session = SessionLocal()

                # check for user in database and return user id if exists or None if not exists 
                if appoinment_type == "all":
                    print("Getting all appointments times")

                    # get all appointments times and doctors names amd return them to the client as json
                    # doctors info are in the Doctor table and appointments info are in the Appointment table
                    # you can use the Appointment.doctor_id to get the doctor name from the Doctor table
                    # code:
                    appointments = db.query(Appointment).all()
                    appointments_times = []
                    for appointment in appointments:
                        appointments_times.append({
                            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
                            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
                            "time": appointment.time
                        })

                    print(appointments_times)                        


                else:
                    print(f"Getting appointments times for type: {appoinment_type}")
                    # like the previous if statement but with the type
                    # code:
                    appointments = db.query(Appointment).filter(Appointment.type == appoinment_type).all()
                    appointments_times = []
                    for appointment in appointments:
                        appointments_times.append({
                            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
                            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
                            "time": appointment.time
                        })
            
            except Exception as e:
                print(f"An error occurred: {e}")

            # stop agent from behaviour
            await self.agent.stop()



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
        
        print("ReturnAvailableTimes behavior added")
        receive_times_behavior = self.ReturnAvailableTimes()
        receive_times_template = Template()
        # receive_times_template.set_metadata("performative", "request")
        receive_times_template.set_metadata("action", "get_appoinments_times")
        self.add_behaviour(receive_times_behavior, receive_times_template)

        print("SetAppoinment added")
        set_time_behavior = self.SetAppoinment()
        set_time_template = Template()
        set_time_template.set_metadata("performative", "request")
        self.add_behaviour(set_time_behavior, set_time_template)


