def convert_btw_lines(x, y):
        x = (x*2)+1
        y = (y*2)+1
        xy = [x, y]
        return xy
#types: type1 = movimiento en x, type2 = movmiento en y,
#type3 = movimiento en y y en x


def determinate_type(coord1, coord2):
	if (coord1[0] != coord2[0] and coord1[1] != coord2[1]):
		type = 3
	elif (coord1[0] != coord2[0] and coord1[1] == coord2[1]):
		type = 1
	elif (coord1[0] == coord2[0] and coord1[1] != coord2[1]):
		type = 2
	return type


def make_path(crd1, crd2):
	t = determinate_type(crd1, crd2)
	crd1 = convert_btw_lines(crd1[0], crd1[1])
	crd2 = convert_btw_lines(crd2[0], crd2[1])
	if (t == 1):
		move1 = crd1                      #va a buscar la pieza a donde esta
		move2 = [crd1[0], crd1[1]+1]      #se pone entre lineas
		move3 = [crd2[0], crd2[1]+1]      #se mueve a la altura en x estando entre lienas
		move4 = crd2                      #se centra en el cuadrado
		moves = [move1, move2, move3, move4]
	elif (t == 2):
		move1 = crd1                      #va a buscar la pieza
		move2 = [crd1[0]+1, crd1[1]]       #se pone entre lienas
		move3 = [crd2[0]+1, crd2[1]]      #se mueve a la altura en y estando entre lienas
		move4 = crd2                      #se centra en el cuadrado
		moves = [move1, move2, move3, move4]
	else:
		move1 = crd1                      #va a buscar la pieza
		move2 = [crd1[0], crd1[1]-1]      #la pone entre lineas
		move3 = [crd2[0]+1, crd1[1]-1]    #se mueve a la altura del destino en el eje x sumandole 1 para que no llevarse por delante las piezas cuando baje
		move4 = [crd2[0]+1, crd2[1]]      #baja estando entre lineas a la altura de destino en y
		move5 = crd2                      #se centra en el cuadrado
		moves = [move1, move2, move3, move4, move5]
	return moves

