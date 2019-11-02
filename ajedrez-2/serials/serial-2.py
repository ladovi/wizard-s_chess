import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate=115200) 
time.sleep(2)
rawString = serial.readline()
print(rawString)
serial.close()