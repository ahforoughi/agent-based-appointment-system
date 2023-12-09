from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal, Appointment, Doctor
from sqlalchemy.orm import Session



# class for the receiver agent (inherits from spade.agent.Agent) 
class SchedulerAgent(Agent):
    def __init__(self, jid, password, action):
        print(f"SchedulerAgent init with action {action}")
        super().__init__(jid, password)

        self.action = action


    class ReturnAvailableTimes(CyclicBehaviour):
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
                    
                    # filter the available times by the status of the appointment
                    # code:
                    appointments = db.query(Appointment).filter(Appointment.status == "empty").all()

                    appointments_times = []
                    for appointment in appointments:
                        appointments_times.append({
                            "appointment_id": appointment.id,
                            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
                            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
                            "time": appointment.time, 
                            "date": appointment.date,
                        })

                    print(appointments_times)                        


                else:
                    print(f"Getting appointments times for type: {appoinment_type}")
                    # like the previous if statement but with the type
                    # first we find the type from the Doctor table
                    # then we find the appointments with the same type from the Appointment table
                    # then we return the appointments times and doctors names to the client as json
                    # code:
                    
                    # find the doctor id from the Doctor table with the appoinment_type
                    doctor_id = db.query(Doctor).filter(Doctor.specialization == appoinment_type).first().id

                    # find the appointments with the same doctor id from the Appointment table
                    appointments = db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

                    appointments_times = []
                    for appointment in appointments:
                        appointments_times.append({
                            "appointment_id": appointment.id,
                            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
                            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
                            "time": appointment.time, 
                            "date": appointment.date,
                        })

                    print(appointments_times)
            
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

            try:
                data = json.loads(msg.body)

                appoinment_id = data["appoinment_id"]
                username = data["username"]
                db: Session = SessionLocal()

                # check for user in database and return user id if exists or None if not exists 
                appointment = db.query(Appointment).filter(Appointment.id == appoinment_id).first()
                if appointment:
                    appointment.patient_id = db.query(Patient).filter(Patient.username == username).first().id

                    # set appointment status to "full"
                    appointment.status = "full"
                    db.commit()
                    print(f"Appointment {appoinment_id} status changed to full.")
                else:
                    print(f"Appointment {appoinment_id} does not exist.")
            
            except Exception as e:
                print(f"An error occurred: {e}")

            # stop agent from behaviour
            await self.agent.stop()


    
    async def setup(self):
        print(f"SchedulerAgent with action {self.action} started")

        if self.action == "get_appointments_times":
            print("ReturnAvailableTimes behavior added")
            receive_times_behavior = self.ReturnAvailableTimes()
            receive_times_template = Template()
            receive_times_template.set_metadata("performative", "request")
            # receive_times_template.set_metadata("action", "get_appoinments_times")
            self.add_behaviour(receive_times_behavior, receive_times_template)
        
        elif self.action == "set_appointment":
            print("SetAppoinment added")
            set_time_behavior = self.SetAppoinment()
            set_time_template = Template()
            set_time_template.set_metadata("performative", "request")
            # set_time_template.set_metadata("action", "set_appointment")
            self.add_behaviour(set_time_behavior, set_time_template)


