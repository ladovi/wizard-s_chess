import serial
#import serial.tools.list_ports

#ports = list(serial.tools.list_ports.comports())
#for p in ports:
#	print(p)
#	print(p[3])
#	if 'Arduino' in p[1]:
#		print('This is the Arduino!')
#		port = p.device
#		print(port)

import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p[0])
arduPort = p[0]
arduino = serial.Serial(arduPort, baudrate='115200')

while True:
    inp = input('INPUT: ')
    arduino.write(bytes(inp, encoding='ascii'))