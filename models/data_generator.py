import json
from datetime import date, time
from models import Patient, Doctor, Appointment, SessionLocal

def get_weekday(date):
    if date.weekday() == 0:
        return "Monday"
    elif date.weekday() == 1:
        return "Tuesday"
    elif date.weekday() == 2:
        return "Wednesday"
    elif date.weekday() == 3:
        return "Thursday"
    elif date.weekday() == 4:
        return "Friday"
    elif date.weekday() == 5:
        return "Saturday"
    else:
        return "Sunday"


# Create sample data for patients
patients_data = [
    {
        "username": "jerry.houston@ucalgary.ca",
        "user_password": "jerry123",
        "first_name": "Jerry",
        "last_name": "Houston",
        "phone": "1234567890",
        "address": "123 Main St"
    },
    {
        "username": "amber.lowe@example.com",
        "user_password": "amber321",
        "first_name": "Amber",
        "last_name": "Lowe",
        "phone": "2345678901",
        "address": "456 Oak St"
    },
]


# Create sample data for doctors
doctors_data = [
    {
        "first_name": "Iona",
        "last_name": "Kaiser",
        "username": "iona.kaiser@example.com",
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
        "username": "harper.marsh@example.com",
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
        "username": "robin.hamilton@example.com",
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
        "username": "carter.hardy@example.com",
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
        "username": "hugh.hammond@example.com",
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
        "username": "charlie.holmes@example.com",
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
        "username": "irven.landry@example.com",
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
        "username": "ellen.reid@example.com",
        "phone": "8765476101",
        "specialization": "massage",
    },
]

# Create sample data for appointments
appointments_data = [
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 1,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(14),
        "status": "empty"
    },
    {
        "patient_id": 2,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 2,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 3,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(14),
        "status": "empty"
    },
    {
        "patient_id": 2,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 4,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 5,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(14),
        "status": "empty"
    },
    {
        "patient_id": 2,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 6,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 12)),
        "date": date(2023, 12, 12),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 12)),
        "date": date(2023, 12, 12),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 12)),
        "date": date(2023, 12, 12),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 12)),
        "date": date(2023, 12, 12),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 12)),
        "date": date(2023, 12, 12),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 14)),
        "date": date(2023, 12, 14),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 14)),
        "date": date(2023, 12, 14),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 14)),
        "date": date(2023, 12, 14),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 14)),
        "date": date(2023, 12, 14),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 19)),
        "date": date(2023, 12, 19),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 19)),
        "date": date(2023, 12, 19),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 19)),
        "date": date(2023, 12, 19),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 19)),
        "date": date(2023, 12, 19),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 19)),
        "date": date(2023, 12, 19),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 21)),
        "date": date(2023, 12, 21),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 21)),
        "date": date(2023, 12, 21),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 21)),
        "date": date(2023, 12, 21),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 21)),
        "date": date(2023, 12, 21),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 26)),
        "date": date(2023, 12, 26),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 26)),
        "date": date(2023, 12, 26),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 26)),
        "date": date(2023, 12, 26),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 26)),
        "date": date(2023, 12, 26),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 26)),
        "date": date(2023, 12, 26),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 28)),
        "date": date(2023, 12, 28),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 28)),
        "date": date(2023, 12, 28),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 28)),
        "date": date(2023, 12, 28),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 7,
        "weekday": get_weekday(date(2023, 12, 28)),
        "date": date(2023, 12, 28),
        "time": time(13),
        "status": "empty"
    },
    {
        "patient_id": 1,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 11)),
        "date": date(2023, 12, 11),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 13)),
        "date": date(2023, 12, 13),
        "time": time(14),
        "status": "empty"
    },
    {
        "patient_id": 2,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 15)),
        "date": date(2023, 12, 15),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 18)),
        "date": date(2023, 12, 18),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 20)),
        "date": date(2023, 12, 20),
        "time": time(14),
        "status": "empty"
    },
    {
        "patient_id": 2,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(10),
        "status": "scheduled"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 22)),
        "date": date(2023, 12, 22),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 25)),
        "date": date(2023, 12, 25),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 1,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(13),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 27)),
        "date": date(2023, 12, 27),
        "time": time(14),
        "status": "empty"
    },
    {
        # "patient_id": 2,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(10),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(11),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(12),
        "status": "empty"
    },
    {
        # "patient_id": NULL,
        "doctor_id": 8,
        "weekday": get_weekday(date(2023, 12, 29)),
        "date": date(2023, 12, 29),
        "time": time(13),
        "status": "empty"
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
