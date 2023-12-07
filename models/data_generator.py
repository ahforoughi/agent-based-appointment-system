import json
from models import Patient, Doctor, Appointment, SessionLocal

# Create sample data for patients
patients_data = [
    {
        "username": "jerry_houston",
        "user_password": "jerry123",
        "first_name": "Jerry",
        "last_name": "Houston",
        "email": "jerry.houston@ucalgary.ca",
        "phone": "1234567890",
        "address": "123 Main St"
    },
    {
        "username": "amber_lowe",
        "user_password": "amber321",
        "first_name": "Amber",
        "last_name": "Lowe",
        "email": "amber.lowe@example.com",
        "phone": "2345678901",
        "address": "456 Oak St"
    },
]


# Create sample data for doctors
doctors_data = [
    {
        "first_name": "Iona",
        "last_name": "Kaiser",
        "email": "iona.kaiser@example.com",
        "phone": "9876543210",
        "specialization": "medical",
        "available_times": json.dumps({
            "Monday": ['10-11', '11-12', '13-14', '14-15', '15-16'], 
            "Wednesday": ['10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Harper",
        "last_name": "Marsh",
        "email": "harper.marsh@example.com",
        "phone": "1676543210",
        "specialization": "medical",
        "available_times": json.dumps({
            "Monday": ['11-12', '13-14', '14-15', '15-16'], 
            "Thursday": ['9-10', '10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Robin",
        "last_name": "Hamilton",
        "email": "robin.hamilton@example.com",
        "phone": "8349032109",
        "specialization": "mental_health",
        "available_times": json.dumps({
            "Monday": ['11-12', '13-14', '14-15', '15-16'], 
            "Wednesday": ['10-11', '11-12', '13-14', '14-15'],
            "Friday": ['9-10', '10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Carter",
        "last_name": "Hardy",
        "email": "carter.hardy@example.com",
        "phone": "9635432109",
        "specialization": "mental_health",
        "available_times": json.dumps({
            "Tuesday": ['11-12', '13-14', '14-15', '15-16'], 
            "Thursday": ['10-11', '11-12', '13-14', '14-15'],
        })
    },
    {
        "first_name": "Hugh",
        "last_name": "Hammond",
        "email": "hugh.hammond@example.com",
        "phone": "8765432109",
        "specialization": "chiropractic",
        "available_times": json.dumps({
            "Monday": ['11-12', '13-14', '14-15', '15-16'], 
            "Wednesday": ['10-11', '11-12', '13-14', '14-15'],
            "Friday": ['9-10', '10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Charlie",
        "last_name": "Holmes",
        "email": "charlie.holmes@example.com",
        "phone": "9765432149",
        "specialization": "chiropractic",
        "available_times": json.dumps({
            "Monday": ['11-12', '13-14', '14-15', '15-16'], 
            "Tuesday": ['10-11', '11-12', '13-14', '14-15'],
            "Thursday": ['11-12', '13-14', '14-15', '15-16'],
            "Friday": ['9-10', '10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Irven",
        "last_name": "Landry",
        "email": "irven.landry@example.com",
        "phone": "8765432590",
        "specialization": "massage",
        "available_times": json.dumps({
            "Tuesday": ['10-11', '11-12', '13-14', '14-15', '15-16'], 
            "Friday": ['9-10', '10-11', '11-12', '13-14'],
        })
    },
    {
        "first_name": "Ellen",
        "last_name": "Reid",
        "email": "ellen.reid@example.com",
        "phone": "8765476101",
        "specialization": "massage",
        "available_times": json.dumps({
            "Monday": ['10-11', '11-12', '13-14', '14-15', '15-16'], 
            "Wednesday": ['10-11', '11-12', '13-14', '14-15'],
            "Saturday": ['9-10', '10-11', '11-12'],
        })
    },
]

# Create sample data for appointments
appointments_data = [
    {
        "patient_id": 1,
        "doctor_id": 8,
        "date": "Monday",
        "time": "10-12",
        "status": "Scheduled"
    },
    {
        "patient_id": 1,
        "doctor_id": 3,
        "date": "Wednesday",
        "time": "14-15",
        "status": "Scheduled"
    },
]


# Session for patients
print("patients started!")
db_patient = SessionLocal()
for patient_data in patients_data:
    patient = Patient(**patient_data)
    db_patient.add(patient)
db_patient.commit()
db_patient.close()
print("patients done!")


# Session for doctors
print("doctors started!")
db_doctor = SessionLocal()
for doctor_data in doctors_data:
    doctor = Doctor(**doctor_data)
    db_doctor.add(doctor)
db_doctor.commit()
db_doctor.close()
print("doctors done!")


# Session for appointments
print("appointment started!")
db_appointment = SessionLocal()
for appointment_data in appointments_data:
    appointment = Appointment(**appointment_data)
    db_appointment.add(appointment)
db_appointment.commit()
db_appointment.close()
print("appointment done!")
