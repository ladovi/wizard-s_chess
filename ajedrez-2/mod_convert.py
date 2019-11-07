import functs as f

def funcion_maxima(cor1, cor2):
	tipo = f.determinate_type(cor1, cor2)
	#print("move type:",tipo)
	moves = f.make_path(cor1, cor2)
	print(moves)
	#magMoves = f.add_magnet(moves)
	#print(magMoves)
	#gline = f.micro_g_code(magMoves[0], 2)
	#gline2 = f.micro_g_code(magMoves[1], 1)
	#print(gline)
	#print(gline2)
	glines = f.g_code_converter(moves)
	print(glines)
	#print(glines)
	#lineasCortadas = acortacion(glines, tipo)
	#print(lineasCortadas)
	#return glines
	#return lineasCortadas
	#send(lineasCortadas)
	return glines
	#home()

	#time.sleep(5)

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
	#for i in lines:
	#	val = find_value(i, typ)
	#	print(val)
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

while True:
	inCoord1 = input("enter coordenate 1 between comas")
	tCoord1 = [int(inCoord1[0]), int(inCoord1[2])]
	inCoord2 = input("enter coordenate 2 between comas")
	tCoord2 = [int(inCoord2[0]), int(inCoord2[2])]
	tipo = f.determinate_type(tCoord1, tCoord2)
	#funcion_maxima(tCoord1, tCoord2)
	caca = funcion_maxima(tCoord1, tCoord2)
	#acort(caca)
	#ind = find_index_letra(caca[2], 'X')
	#print(ind)
	#acort(caca, tipo)
	#valin = find_value(caca[2], 'X')
	#print(valin)

	tod_lineas = acort(caca, tipo)
	#print(tod_lineas)
	#print(find_value(caca, 'X'))
	print(add_gMagnet(tod_lineas))
	
	

