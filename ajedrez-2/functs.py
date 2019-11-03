import time
import serial



def convert_btw_lines(x, y):
        x = (x*2)+1
        y = (y*2)+1
        xy = [x, y]
        return xy
#types: type1 = movimiento en x, type2 = movmiento en y,
#type3 = movimiento en y y en x


def determinate_type(coord1, coord2):
	if (coord1[0] != coord2[0] and coord1[1] != coord2[1]):
		ty = 3
	elif (coord1[0] != coord2[0] and coord1[1] == coord2[1]):
		ty = 1
	elif (coord1[0] == coord2[0] and coord1[1] != coord2[1]):
		ty = 2
	return ty


#def wait_for_answer():
#	ser = serial.Serial('/dev/ttyACM0', baudrate=115200) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
#	ser.flushInput()
#	ser.flushOutput()
#	data_raw = ser.readline()
 # 	print(data_raw)


def make_path(crd1, crd2):
	t = determinate_type(crd1, crd2)
	crd1 = convert_btw_lines(crd1[0], crd1[1])
	crd2 = convert_btw_lines(crd2[0], crd2[1])
	if (t == 1):
		move1 = crd1                      #va a buscar la pieza a donde esta
		#se prende el electroiman
		move2 = [crd1[0], crd1[1]+1]      #se pone entre lineas
		move3 = [crd2[0], crd2[1]+1]      #se mueve a la altura en x estando entre lienas
		move4 = crd2                      #se centra en el cuadrado
		#se apaga el electroiman
		moves = [move1, move2, move3, move4]
	elif (t == 2):
		move1 = crd1                      #va a buscar la pieza
		#se prende iman
		move2 = [crd1[0]+1, crd1[1]]       #se pone entre lienas
		move3 = [crd2[0]+1, crd2[1]]      #se mueve a la altura en y estando entre lienas
		move4 = crd2                      #se centra en el cuadrado
		#se apaga iman
		moves = [move1, move2, move3, move4]
	else:
		move1 = crd1                      #va a buscar la pieza
		#se prende iman
		move2 = [crd1[0], crd1[1]-1]      #la pone entre lineas
		move3 = [crd2[0]+1, crd1[1]-1]    #se mueve a la altura del destino en el eje x sumandole 1 para que no llevarse por delante las piezas cuando baje
		move4 = [crd2[0]+1, crd2[1]]      #baja estando entre lineas a la altura de destino en y
		move5 = crd2                      #se centra en el cuadrado
		#se apaga iman
		moves = [move1, move2, move3, move4, move5]
	return moves

def add_magnet(mov):
	mov.insert(1, 1)
	mov.append(0)
	return mov

def micro_g_code(line, tam):
	g = "G"
	x = "X"
	y = "Y"
	esp = " "

	if (tam > 1):
		gLine = g+"01"+esp+x+str(line[0])+y+str(line[1])
	else:
		if (line == 1):
			gLine = "M3"
		else:
			gLine = "M4"
	return gLine




def g_code_converter(m):

	#for i in len(m):
	#	gLines.append(micro_g_code(m[i]))
	#return gLines

	#gLines = ["g"]
	#for i in len(m):
	#i = 0
	#while(i < len(m)):
	#	gLines.append(micro_g_code(m[i]), len(m))
	#	i += 1
	#return gLines
	#print(m)
	allLines = []
	for i in m:
		allLines.append(micro_g_code(i, len(list(str(i)))))
	return allLines

def send(val):
	arduino = serial.Serial('/dev/ttyACM0', baudrate=115200)
	
	for z in val:
		arduino.write(bytes("\r\n\r\n", encoding='ascii'))
		arduino.write(bytes(str(z), encoding='ascii'))
		arduino.write(bytes("\r\n\r\n", encoding='ascii'))
		print(z)
		time.sleep(.5)
		#wait_for_answer()
		time.sleep(.5)

