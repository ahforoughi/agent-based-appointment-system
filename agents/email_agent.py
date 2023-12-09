import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json
from models import Patient, SessionLocal
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
				print("Message received with content: {}".format(msg.body))
			else:
				print("Did not received any message after 10 seconds")

			try:
				data = json.loads(msg.body)
				
				username = data["username"]
					
				db: Session = SessionLocal()

				# check for user in database and return user id if exists or None if not exists
				user = db.query(Patient).filter(Patient.username == username).first()

				if user:
					print(f"User {username} exists.")

					# Compose email
					email_from = smtp_username
					email_to = str(username)
					email_subject = "your appointment is confirmed"
					email_body = "Hello, your appointment is confirmed."

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
		b = self.SendEmail()
		template = Template()
		template.set_metadata("performative", "inform")		
		self.add_behaviour(b, template)
