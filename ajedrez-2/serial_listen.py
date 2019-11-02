import serial

ser = serial.Serial('/dev/ttyACM0', baudrate=115200) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while (True):
  data_raw = ser.readline()
  print(data_raw)