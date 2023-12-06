from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)  
    address = Column(String)  

    appointments = relationship('Appointment', back_populates='patients')


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)  
    specialization = Column(String)  
    available_times = Column(String)  

    appointments = relationship('Appointment', back_populates='doctors')


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date = Column(String)
    time = Column(String)
    status = Column(String)


    patients = relationship('Patient', back_populates='appointments')
    doctors = relationship('Doctor', back_populates='appointments')


# Separate database files for each class
DATABASE_URL_PATIENT = "sqlite:///./database/patients.db"
DATABASE_URL_DOCTOR = "sqlite:///./database/doctors.db"
DATABASE_URL_APPOINTMENT = "sqlite:///./database/appointments.db"

engine_patient = create_engine(DATABASE_URL_PATIENT)
engine_doctor = create_engine(DATABASE_URL_DOCTOR)
engine_appointment = create_engine(DATABASE_URL_APPOINTMENT)

# Create tables
Base.metadata.create_all(bind=engine_patient)
Base.metadata.create_all(bind=engine_doctor)
Base.metadata.create_all(bind=engine_appointment)

# Session creation (you can create separate sessions for each engine if needed)
SessionLocal_patient = sessionmaker(autocommit=False, autoflush=False, bind=engine_patient)
SessionLocal_doctor = sessionmaker(autocommit=False, autoflush=False, bind=engine_doctor)
SessionLocal_appointment = sessionmaker(autocommit=False, autoflush=False, bind=engine_appointment)

