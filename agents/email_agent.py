import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal, Appointment, Doctor
from sqlalchemy.orm import Session
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create SMTP connection
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "zahraarabinarei1998@gmail.com"
smtp_password = "yofxuonbqbevoqsw"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    print("Ready for message")
except Exception as e:
    print("Error:", str(e))





# class for the receiver agent (inherits from spade.agent.Agent) 
class EmailAgent(Agent):

	class SendEmail(CyclicBehaviour):
		async def run(self):
			print("SendEmail running")

			msg = await self.receive(timeout=10) # wait for a message for 10 seconds
			if msg:
				print("Message received in SendEmail with content: {}".format(msg.body))
			else:
				print("Did not received any message after 10 seconds")

			try:
				data = json.loads(msg.body)
				
				username = data["username"]
					
				db: Session = SessionLocal()

				# check for user in database and return user id if exists or None if not exists
				user = db.query(Patient).filter(Patient.username == username).first()

				# retrive the appointment time from the database fot the user
				appointment = db.query(Appointment).filter(Appointment.patient_id == user.id).first()

				# retrive the appointment time from the database fot the user
				doctor = db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first()

				# remove the 00.00.00 from the date
				date = str(appointment.date).split(" ")[0]



				if user:
					print(f"User {username} exists.")

					# Compose email
					email_from = smtp_username
					email_to = str(username)
					email_subject = "your appointment is confirmed"
					
					email_body = f'''
					<img src="http://161.35.11.188:8090/media/images/d537d830-b0a1-4e33-bbf8-17eabd3a240f.jpg"/> <br/><br/>
					Hello {user.first_name}, <br/><br/>
					This is a confirmation for your appointment at WellBook UofC on {appointment.weekday} {date}, at {appointment.time} with doctor {doctor.first_name} {doctor.last_name}. <br/> <br/>
					Thank you. View details of your appointment at WellBook UofC.
					'''

					msg = MIMEMultipart()
					msg["From"] = email_from
					msg["To"] = email_to
					msg["Subject"] = email_subject
					msg.attach(MIMEText(email_body, "html"))
					server.sendmail(email_from, email_to, msg.as_string())
					server.quit()
					print("Email sent successfully.")

				else:
					print(f"User {username} does not exist.")

			except Exception as e:
				print(f"An error occurred: {e}")

			# stop agent from behaviour
			await self.agent.stop()
				
	class SendReminder(CyclicBehaviour):
		async def run(self):
			print("SendReminder running")

			msg = await self.receive(timeout=10)
			if msg:
				print("Message received in SendReminder with content: {}".format(msg.body))
			else:
				print("Did not received any message after 10 seconds")

			
			
			try:
				data = json.loads(msg.body)
				
				username = data["username"]
					
				db: Session = SessionLocal()

				# check for user in database and return user id if exists or None if not exists
				user = db.query(Patient).filter(Patient.username == username).first()


				# retrive the appointment time from the database fot the user
				appointment = db.query(Appointment).filter(Appointment.patient_id == user.id).first()

				# retrive the appointment time from the database fot the user
				doctor = db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first()

				# remove the 00.00.00 from the date
				date = str(appointment.date).split(" ")[0]


				if user:
					print(f"User {username} exists.")

					# Compose email
					email_from = smtp_username
					email_to = str(username)
					email_subject = "Appointment Reminder"
					email_body = f'''
					<img src="http://161.35.11.188:8090/media/images/d537d830-b0a1-4e33-bbf8-17eabd3a240f.jpg"/> <br/><br/>
					Hello {user.first_name}, <br/><br/>
					This is a reminder for your appointment at WellBook UofC on {appointment.weekday} {date}, at {appointment.time} with doctor {doctor.first_name} {doctor.last_name}. <br/> <br/>
					Thank you. View details of your appointment at WellBook UofC.
					'''

					msg = MIMEMultipart()
					msg["From"] = email_from
					msg["To"] = email_to
					msg["Subject"] = email_subject
					msg.attach(MIMEText(email_body, "html"))
					server.sendmail(email_from, email_to, msg.as_string())
					server.quit()
					print("Email sent successfully.")

				else:
					print(f"User {username} does not exist.")

			except Exception as e:
				print(f"An error occurred: {e}")

			# stop agent from behaviour
			await self.agent.stop()


	async def setup(self):
		print("EmailAgent started")
		beh_sendconfirm = self.SendEmail()
		template_sendconfirm = Template()
		template_sendconfirm.set_metadata("performative", "inform")
		template_sendconfirm.set_metadata("action", "email-confirmation")	
		self.add_behaviour(beh_sendconfirm, template_sendconfirm)



		b_reminder = self.SendReminder()
		template_reminder = Template()
		template_reminder.set_metadata("performative", "inform")
		template_reminder.set_metadata("action", "email-reminder")	
		self.add_behaviour(b_reminder, template_reminder)