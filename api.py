# Import FastAPI
from fastapi import FastAPI
import subprocess
import sys
from models import *
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware
import datetime

# config logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create an instance of the FastAPI class
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a root `/` endpoint
@app.get("/")
def root():
    logger.info("in root")
    return {"message": "Hello World"}



# Define the data model
class User(BaseModel):
    username: str
    phone: str
    password: str
    firstname: str
    lastname: str

# Define a root `/register` endpoint which receives `username`, `email`, `phone` and `password` parameters
@app.post("/register")
async def register_user(user: User):
    firstname = user.firstname
    lastname = user.lastname
    username = user.username
    phone = user.phone
    password = user.password

    output = subprocess.check_output(["python", "main.py", "--register", 
                                    firstname, lastname, username, phone, password])
    result = output.splitlines()[-1].decode("utf-8")

    print(result)

    # return 200 code if the user registered successfully otherwise return 500 code
    if "Registered new user:" in result:
        return JSONResponse(content={"message": "User Registered"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User Registeration Failed"}, status_code=400)



class LoginData(BaseModel):
    username: str
    password: str

# Define a root `/login` endpoint which receives just `username` and `password` parameters
@app.post("/login")
async def login(login_data: LoginData):
    username = login_data.username
    password = login_data.password

    output = subprocess.check_output(["python", "main.py", "--login", username, password])
    result = output.splitlines()[-1].decode("utf-8")



    print(result)

    if "logged in" in result:
        # retrive the user info from the database
        db: Session = SessionLocal()
        user = db.query(Patient).filter(Patient.username == username).first()
        db.close()

        # create the json response from the user info
        user_info = {
            "username": user.username,
            "phone": user.phone,
            "firstname": user.first_name,
            "lastname": user.last_name,
        }
        
        return JSONResponse(content={"message": "User Logged in", "user_info": user_info}, status_code=200)
    else:
        return JSONResponse(content={"message": "User login Failed"}, status_code=400)


class AppointmentType(BaseModel):
    appoinment_type: str

def convert_to_json(var):
    # Step 1: Parse the string
    parsed_data = eval(var)

    # Step 2: Handle datetime objects
    for item in parsed_data:
        if 'date' in item:
            item['date'] = item['date'].isoformat()
        if 'time' in item:
            item['time'] = item['time'].isoformat()

    # Step 3: Convert to JSON
    return parsed_data

@app.post("/appointments")
async def get_appointments_times(request: AppointmentType):
    type_appoin = request.appoinment_type
    print(type_appoin)

    # check if the request body is empty
    if type_appoin == "all":
        output = subprocess.check_output(["python", "main.py", "--get_appoinments_times", type_appoin])
    else:
        # get the type from the request body
        output = subprocess.check_output(["python", "main.py", "--get_appoinments_times", type_appoin])

    result = output.splitlines()[-1].decode("utf-8")
    print(type(result))
    print(result)
    result = convert_to_json(result)

    return JSONResponse(content=result, status_code=200)



class AppointmentID(BaseModel):
    appointment_id: int
    username: str

@app.post("/set-appointments")
async def set_appointments_times(request: AppointmentID):
    id_app = str(request.appointment_id)
    username = request.username
    logger.info(request)

    output = subprocess.check_output(["python", "main.py", "--set_appoinment", id_app, username])
    result = output.splitlines()[-1].decode("utf-8")

    if "full" in result:
        return JSONResponse(content={"message": "Appointment is set"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Appointment setting failed"}, status_code=400)

class EmailUser(BaseModel):
    username: str

# an endpoint to get all future appointments for a user
@app.post("/get-appointments-user")
async def get_appointments_times(request: EmailUser):
    username = request.username

    # query the database for the user appointments in the appointment table
    db: Session = SessionLocal()

    # find the user id from the Patient table
    user_id = db.query(Patient).filter(Patient.username == username).first().id

    # find the appointments with the same user id from the Appointment table
    appointments = db.query(Appointment).filter(Appointment.patient_id == user_id).all()

    # return the appointments as json and convert the datetime objects to string
    appointments_times = []
    for appointment in appointments:
        appointments_times.append({
            "appointment_id": appointment.id,
            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
            "time": appointment.time.isoformat(),
            "date": appointment.date.isoformat(),
        })
    
    db.close()
    return JSONResponse(content=appointments_times, status_code=200)

@app.post("/send-email")
async def get_appointments_times(request: EmailUser):
    username = request.username
    print(type)


    output = subprocess.check_output(["python", "main.py", "--send_email", username])

    result = output.splitlines()[-1].decode("utf-8")
    print(result)
    # return result
    # return the output as json 
    return JSONResponse(content=json.dumps(result), status_code=200)


from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

def send_email_later(username):
    print("Sending email")
    subprocess.check_output(["python", "main.py", "--send_reminder", username])


class remindUser(BaseModel):
    username: str
    date: datetime.datetime

scheduler = BackgroundScheduler(timezone="America/Edmonton")
scheduler.start()

@app.post("/send-reminder")
async def send_reminder(request: remindUser):
     # Calculate when to send the email (24 hours before appointment time)
    # appointment_time = datetime.datetime.now().replace(hour=20, minute=7)
    appointment_time = datetime.datetime.now()  # December 10, 2023, 15:30

    print(appointment_time)

    # calcualte the new time based on appointment time 
    send_time = appointment_time + datetime.timedelta(minutes=1)
    send_time += datetime.timedelta(hours=1)


    print(send_time)
    scheduler.add_job(send_email_later, 'date', run_date=send_time, args=[request.username])
        


# Make sure to shut down the scheduler when the application exits
import atexit
atexit.register(lambda: scheduler.shutdown())






# Define a root for reading from the database
@app.get("/db")
async def db():
    # get the user from the database
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}