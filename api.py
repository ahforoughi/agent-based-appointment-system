# Import FastAPI
from fastapi import FastAPI
import subprocess
import sys
from models import *
from pydantic import BaseModel, EmailStr


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


    return {"result": result}



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

    return {"result": result}






# Define a root for reading from the database
@app.get("/db")
async def db():
    # get the user from the database
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}