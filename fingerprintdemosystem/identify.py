from fingerprint import FingerprintSensor
import sqlite3
from datetime import datetime

def mark_attendance():
    sensor = FingerprintSensor()
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    student_id = sensor.identify_fingerprint()
    if student_id:
        now = datetime.now()
        cur.execute("INSERT INTO attendance (student_id, time) VALUES (?, ?)", (student_id, now))
        conn.commit()
        student = cur.execute("SELECT name FROM students WHERE id = ?", (student_id,)).fetchone()
        print(f"[✓] Attendance marked for {student[0]} at {now}")
    else:
        print("[!] Fingerprint not recognized.")

    sensor.close()
    conn.close()