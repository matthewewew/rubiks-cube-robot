import serial
import time

class CubeBot:
    def __init__(self, port='COM3', baud=115200):  # change COM3 to your port
        self.ser = serial.Serial(port, baud, timeout=5)
        time.sleep(2)  # wait for ESP32 reset
        print("Connected to ESP32")

    def send_sequence(self, moves):
        line = ' '.join(moves) + '\n'
        self.ser.write(line.encode())
        print(f"Sent: {line.strip()}")

        while True:
            response = self.ser.readline().decode().strip()
            if response:
                print(f"ESP32: {response}")
            if response == "DONE":
                break

    def close(self):
        self.ser.close()