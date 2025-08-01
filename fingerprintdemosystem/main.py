import tkinter as tk
from tkinter import simpledialog
from enroll import enroll_student
from identify import mark_attendance

root = tk.Tk()
root.title("Fingerprint Attendance System")
root.geometry("400x300")

def enroll_gui():
    name = simpledialog.askstring("Name", "Enter Student Name")
    roll = simpledialog.askstring("Roll", "Enter Roll Number")
    if name and roll:
        enroll_student(name, roll)

def attendance_gui():
    mark_attendance()

tk.Label(root, text="Fingerprint Attendance", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Enroll Student", command=enroll_gui, width=20).pack(pady=10)
tk.Button(root, text="Mark Attendance", command=attendance_gui, width=20).pack(pady=10)

root.mainloop()