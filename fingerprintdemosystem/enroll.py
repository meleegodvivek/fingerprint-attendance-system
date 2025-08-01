from fingerprint import FingerprintSensor
import sqlite3

def enroll_student(name, roll):
    sensor = FingerprintSensor()
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    student_id = cur.execute("SELECT COUNT(*) FROM students").fetchone()[0] + 1
    if sensor.enroll_fingerprint(student_id):
        cur.execute("INSERT INTO students (id, name, roll) VALUES (?, ?, ?)", (student_id, name, roll))
        conn.commit()
        print("[+] Enrollment successful.")
    else:
        print("[!] Enrollment failed.")
    
    sensor.close()
    conn.close()