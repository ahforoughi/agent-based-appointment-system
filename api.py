# Import FastAPI
from fastapi import FastAPI
import subprocess
import sys
from models import *
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware


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
    email: EmailStr

# Define a root `/register` endpoint which receives `username`, `email`, `phone` and `password` parameters
@app.post("/register")
async def register_user(user: User):
    username = user.username
    email = user.email
    phone = user.phone
    password = user.password

    output = subprocess.check_output(["python", "main.py", "--register", username, email, phone, password])
    result = output.splitlines()[-1].decode("utf-8")

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

    if "logged in" in result:
        return JSONResponse(content={"message": "User Logged in"}, status_code=200)
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


# Define a root for reading from the database
@app.get("/db")
async def db():
    # get the user from the database
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}