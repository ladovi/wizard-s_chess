import time
import serial



def convert_btw_lines(x, y):
        x = (x*2)+1
        y = (y*2)+1
        xy = [x, y]
        #print(xy)
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
		move3 = [crd2[0]-1, crd1[1]-1]    #se mueve a la altura del destino en el eje x sumandole 1 para que no llevarse por delante las piezas cuando baje
		move4 = [crd2[0]-1, crd2[1]]      #baja estando entre lineas a la altura de destino en y
		move5 = crd2                      #se centra en el cuadrado
		#se apaga iman
		moves = [move1, move2, move3, move4, move5]
	return moves

def val_path(line, letra):
	
	indX = find_index_letra(line, 'X')
	indY = find_index_letra(line, 'Y')
	val = ''
	if (letra == 'X'):
		i = indX
		while (i < indY):
			val = val+line[i]
			i += 1
			
	else:
		i = indY
		while (i < len(line)):
			val = val+line[i]
			i += 1
	return val



	


def add_magnet(mov):
	mov.insert(1, 1)
	mov.append(0)
	return mov

def mayor(linexd):
	if (len(linexd) > 2):
		may = True
	return may

def micro_g_code(line, tam):
	g = "G"
	x = "X"
	y = "Y"
	esp = " "

	if (tam > 1):
		gLine = g+"91"+esp+x+str(line[0])+y+str(line[1])
		#if (len(str(line[0])) > 1):
			#xVal = str(line[0])
			#gline = g+"91"+esp+x+xVal+esp+y+yVal
		#	gLine = g+"91"+esp+x+str(line[0])+y+str(line[1])
		#if (len(str(line[1])) > 1):
		#	yVal = str(line[1])
	else:
		if (line == 1):
			gLine = "M3"
		else:
			gLine = "M4"
	return gLine

def find_index_letra(line, letra):
	index = 0
	for i in line:
		if (i == letra):
			esp = index
			break
		else:
			index += 1
	return index

def find_value(line, letra):
	
	indX = find_index_letra(line, 'X')
	indY = find_index_letra(line, 'Y')
	val = ''
	if (letra == 'X'):
		i = indX
		while (i < indY):
			val = val+line[i]
			i += 1
			
	else:
		i = indY
		while (i < len(line)):
			val = val+line[i]
			i += 1
	return val





def acort(lines, typ):
	allLines = []

	if (typ == 1):
		allLines.append(lines[0])
		allLines.append('G91 '+find_value(lines[1], 'Y'))
		allLines.append('G91 '+find_value(lines[2], 'X'))
		allLines.append('G91 '+find_value(lines[3], 'Y'))
	elif (typ == 2):
		allLines.append(lines[0])
		allLines.append('G91 '+find_value(lines[1], 'X'))
		allLines.append('G91 '+find_value(lines[2], 'Y'))
		allLines.append('G91 '+find_value(lines[3], 'X'))
	else:
		allLines.append(lines[0])
		allLines.append('G91 '+find_value(lines[1], 'Y'))
		allLines.append('G91 '+find_value(lines[2], 'X'))
		allLines.append('G91 '+find_value(lines[3], 'Y'))
		allLines.append('G91 '+find_value(lines[4], 'X'))
	return allLines

def add_gMagnet(tira_lineas):
	tira_lineas.insert(1, 'M4')
	tira_lineas.append('M3')
	return tira_lineas



#def acortacion(lineas, tipo):
#	lineasFinal = []
#
#	if (tipo == 1):
#		linea1 = micro_acorte(lineas[2], 'x')
#		linea2 = micro_acorte(lineas[3], 'y')
#		linea3 = micro_acorte(lineas[4], 'x')
#		lineasFinal.append(lineas[0])
#		lineasFinal.append(lineas[1])
#		lineasFinal.append(linea1)
#		lineasFinal.append(linea2)
#		lineasFinal.append(linea3)
#		lineasFinal.append(lineas[5])
#	elif (tipo == 2):
#		linea1 = micro_acorte(lineas[2], 'y')
#		linea3 = micro_acorte(lineas[4], 'y')
#
#		lineasFinal.append(lineas[0])
#		lineasFinal.append(lineas[1])
#		lineasFinal.append(linea1)
#		lineasFinal.append(linea2)
#		lineasFinal.append(linea3)
#	linea2 = micro_acorte(lineas[3], 'y')
#		linea3 = micro_acorte(lineas[4], 'x')
#		linea4 = micro_acorte(lineas[5], 'y')
#
#		lineasFinal.append(lineas[0])
#		lineasFinal.append(lineas[1])
#		lineasFinal.append(linea1)
#		lineasFinal.append(linea2)
#		lineasFinal.append(linea3)
#		lineasFinal.append(linea4)
#		lineasFinal.append(lineas[6])
#
#	return lineasFinal 


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
	'''
	ports = list(serial.tools.list_ports.comports())
	for p in ports:
    	#print p
		if "Arduino" in p[1]:
			arduino = serial.Serial(p[0], baudrate=115200)
	
	tempN = 3
	tempF = 5
	'''
	arduino = serial.Serial('dev/ttyACM0', baudrate=115200)
	

	arduino.write(bytes("\r\n\r\n", encoding='ascii'))
	arduino.write(bytes("M4", encoding='ascii'))

	for z in val:
		
		arduino.write(bytes("\r\n\r\n", encoding='ascii'))
		arduino.write(bytes(str(z), encoding='ascii'))
		arduino.write(bytes("\r\n\r\n", encoding='ascii'))
		print(z)
		time.sleep(3)
		#wait_for_answer()
		time.sleep(.5)

def home(tira):
	tam = len(tira)
	ultTira = tira[tam-1]
	y = find_value(ultTira, 'Y')
	#y = list(y.insert(1, '-'))
	y = y.replace('Y', '-')
	x = find_value(ultTira, 'X')
	#x = list(x.insert(1, '-'))
	x = x.replace('X', '-')
	ultTira = 'G91 '+'X'+x+'Y'+y
	#print(ultTira)
	return ultTira



def resta(line1, line2, let):
	a = find_value(line1, let)
	b = find_value(line2, let)
	print("despues del find_value:", a, b)
	a = a.replace(let, '')
	b = b.replace(let, '')
	print("despues del replace:", a, b)
	res = int(b) - int(a)
	#print(a, b)
	#print(len(a), len(b))
	#print(res)
	return res 

def mkPath2(path, tipo):
	#print(len(path))
	if (tipo == 1):
		m1 = resta(path[1], path[3], 'Y')
		m2 = resta(path[3], path[4], 'X')
		m3 = resta(path[4], path[5], 'Y')
		l1 = 'G91 Y'+str(m1)
		l2 = 'G91 X'+str(m2)
		l3 = 'G91 Y'+str(m3)
		fixedPath = [path[0], path[1], path[2], l1, l2, l3, path[6]]
	elif (tipo == 2):
		m1 = resta(path[1], path[3], 'X')
		m2 = resta(path[3], path[4], 'Y')
		m3 = resta(path[4], path[5], 'X')
		l1 = 'G91 X'+str(m1)
		l2 = 'G91 Y'+str(m2)
		l3 = 'G91 X'+str(m3)
		fixedPath = [path[0], path[1], path[2], l1, l2, l3, path[6]]
	else:
		m1 = resta(path[1], path[3], 'Y')
		m2 = resta(path[3], path[4], 'X')
		m3 = resta(path[4], path[5], 'Y')
		m4 = resta(path[5], path[6], 'X')
		l1 = 'G91 Y'+str(m1)
		l2 = 'G91 X'+str(m2)
		l3 = 'G91 Y'+str(m3)
		l4 = 'G91 X'+str(m4)
		fixedPath = [path[0], path[1], path[2], l1, l2, l3, l4, path[7]]
	return fixedPath

def goodPath(path, tipo):
	if (tipo == 1):
		m1 = resta(path[1], path[3], 'X')
		l1 = 'G91 X'+str(m1)
		fixedPath = [path[0], path[1], path[2], l1, path[4], path[5]]
	elif (tipo == 2):
		m1 = resta(path[1], path[3], 'Y')
		l1 = 'G91 Y'+str(m1)
		fixedPath = [path[0], path[1], path[2], l1, path[4], path[5]]
	else:
		m1x = resta(path[1], path[3], 'X')
		m1y = resta(path[1], path[3], 'Y')
		l1 = 'G91 X'+str(m1x)+'Y'+str(m1y)
		fixedPath = [path[0], path[1], path[2], l1, path[4], path[5]]
	return fixedPath


def funcion_maxima(cor1, cor2):
	tipo = determinate_type(cor1, cor2)
	x1 = int(cor1[0])
	x2 = int(cor2[0])
	y1 = int(cor1[1])		
	y2 = int(cor2[1])
	if (tipo == 3 and x2-x1 != y2-y1):		
		moves = make_path(cor1, cor2)	
		glines = g_code_converter(moves)
		print(glines)
		tod_lineas = glines
		h = home(glines)
		#tod_lineas = acort(glines, tipo)
		tod_lineas = add_gMagnet(tod_lineas)
		tod_lineas.insert(0, "G00 X0Y0")
		

		print("home: "+h)
		tod_lineas.append(h)
		print("tira de lineas:", tod_lineas)
		tod_lineas = mkPath2(tod_lineas, tipo)
		tod_lineas.append(h)
	else:
		lss = []
		lss.append(cor1)
		lss.append(cor2)
		glines = g_code_converter(lss)
		h = home(glines)
		print(glines)
		if (tipo == 1):
			v = find_value(glines[1], 'Y')
			lineaCambiada = glines[1].replace(v, "")
			glines[1] = lineaCambiada
		elif (tipo == 2):
			v = find_value(glines[1], 'X')
			lineaCambiada = glines[1].replace(v, "")
			glines[1] = lineaCambiada
		tod_lineas = add_gMagnet(glines)
		tod_lineas.insert(0, 'G00 X0Y0')
		
		tod_lineas.append(h)
		print("tod_lineas:", tod_lineas)
		tod_lineas = goodPath(tod_lineas, tipo)
		#tod_lineas = mkPath2(tod_lineas, tipo)
		#tod_lineas = acort(glines, tipo)

	return tod_lineas

	'''
	#print("move type:",tipo)
	#moves = make_path(cor1, cor2)
	#print(moves)
	#magMoves = add_magnet(moves)
	#print(magMoves)
	#gline = micro_g_code(moves, 2)
	#gline2 = micro_g_code(magMoves[1], 1)
	#print(gline)
	#print(gline2)
	#glines = g_code_converter(moves)
	print(glines)
	#lineasCortadas = acortacion(glines, tipo)
	#print(lineasCortadas)

	#return lineasCortadas
	#send(lineasCortadas)

	#home()
	tod_lineas = glines
	#tod_lineas = acort(glines, tipo)
	tod_lineas = add_gMagnet(tod_lineas)
	tod_lineas.insert(0, "G00 X0Y0")
	h = home(glines)

	print(h)
	tod_lineas.append(h)
	print(tod_lineas)
	#add_gMagnet(gl)
	#print(gl)
	#print(glines)
	#glines.insert(0, 'G91 X0Y0')
	#print(glines)
	#glines = glines.append(home(gl))
	tod_lineas = mkPath2(tod_lineas, tipo)
	#print(glines)
	return tod_lineas
	#fLineas = mkPath2(tod_lineas, tipo)
	#send(tod_lineas)
	#return fLineas
	#print(tod_lineas)
	#print(find_value(caca, 'X'))
	#print(add_gMagnet(tod_lineas))

	#time.sleep(5)
	'''

