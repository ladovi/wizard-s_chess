import serial


ser = serial.Serial('/dev/ttyACM0', baudrate=115200)

ser.flushInput()
ser.flushOutput()



while (True):
	indata = ser.readline()
	print(indata)
	data = input("INPUT: ")
	ser.write(bytes(data, encoding='ascii'))
	
