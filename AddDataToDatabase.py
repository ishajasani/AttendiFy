import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-6eb03-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "21DCS001" : {
        "name": "Bill Gates",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2024-10-14 00:54:34"
    },
"21DCS003" : {
        "name": "Anne Hath",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 30,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-10-14 00:52:34"
    },
"21DCS031" : {
        "name": "Isha Jasani",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 40,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-10-14 00:50:34"
    },
"21DCS065" : {
        "name": "Dreemi Panchal",
        "major": "CSE",
        "starting_year": 2021,
        "total_attendance": 20,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-10-14 00:57:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)