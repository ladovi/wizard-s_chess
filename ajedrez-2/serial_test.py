import serial
import serial.tools.list_ports


#ports = list(serial.tools.list_ports.comports())
#for p in ports:
#    print(p)
#    print(p[3])
#    if "Arduino" in p[1]:
#        print("This is an Arduino!")
#      port = p.device
#      print(port)


arduino = serial.Serial('/dev/ttyACM0', baudrate=115200)

while True:
    pito = input("INPUT: ")
    arduino.write(bytes(pito, encoding='ascii'))