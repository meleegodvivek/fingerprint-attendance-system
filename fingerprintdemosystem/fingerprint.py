import serial
import time

class FingerprintSensor:
    def __init__(self, port='COM3', baudrate=57600):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

    def send_command(self, command):
        self.ser.write(command)
        response = self.ser.read(12)
        return response

    def enroll_fingerprint(self, id):
        # Send enrollment command to sensor (simplified)
        print(f"[+] Enrolling ID: {id}")
        # Use actual protocol commands depending on sensor
        return True

    def identify_fingerprint(self):
        # Send identification command
        print("[*] Waiting for fingerprint...")
        # Return dummy ID for now
        return 1

    def close(self):
        self.ser.close()