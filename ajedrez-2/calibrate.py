import serial as ser
import serial.tools.list_ports
import time

#ports = list(serial.tools.list_ports.comports())
#for p in ports:
#    print(p)
#    if "Arduino" in p[1]:
#        arduino = serial.Serial(p[0], baudrate=115200)
#        print("arduino seteado a", p[0])

arduino = serial.Serial('/dev/ttyACM0', baudrate=115200)
	

while True:
	cant = input("cantidad de repeticiones: ")
	i = 0
	while (i < int(cant)):
		arduino.write(bytes("\r\n\r\n", encoding='ascii'))
		arduino.write(bytes("G91 Y1", encoding='ascii'))
		i+=1
		time.sleep(1.5)



