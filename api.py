# Import FastAPI
from fastapi import FastAPI
import subprocess
import sys
from models import *
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse
import json
# config logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create an instance of the FastAPI class
app = FastAPI()

# Define a root `/` endpoint
@app.get("/")
async def root():
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

@app.post("/appointments")
async def get_appointments_times(request: AppointmentType):
    type = request.appoinment_type
    print(type)

    # check if the request body is empty
    if type == "all":
        output = subprocess.check_output(["python", "main.py", "--get_appoinments_times", type])
    else:
        # get the type from the request body
        data = json.loads(request.body)
        type = data["type"]
        output = subprocess.check_output(["python", "main.py", "--get_appoinments_times", type])

    result = output.splitlines()[-1].decode("utf-8")
    print(result)
    # return result
    # return the output as json 
    return JSONResponse(content=json.dumps(result), status_code=200)



class AppointmentID(BaseModel):
    appointment_id: str

@app.post("/set-appointments")
async def set_appointments_times(request: AppointmentID):
    id = request.appointment_id

    output = subprocess.check_output(["python", "main.py", "--set_appoinment", id])
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

    # return the appointments as json
    appointments_times = []
    for appointment in appointments:
        appointments_times.append({
            "appointment_id": appointment.id,
            "doctor_specilization": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().specialization,
            "doctor_name": db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first().first_name,
        })
    
    db.close()
    return JSONResponse(content=json.dumps(appointments_times), status_code=200)

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


# Define a root for reading from the database
@app.get("/db")
async def db():
    # get the user from the database
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}