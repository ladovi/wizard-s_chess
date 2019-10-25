


home = [0,0]

def convert(x, y):
	x = (x*2)+1
	y = (y*2)+1
	xy = [x, y]
	return xy

prevCoords = [home, home]

#inp = input()

#modCoorX = int(inp[0])
#modCoorY = int(inp[2])

#modCoorX = place1[0]
#modCoorY = place1[1] 

#modCoorX = (modCoorX*2)+1
#modCoorY = (modCoorY*2)+1

#coor1 = [modCoorX, modCoorY]

while (true):

	coor1 = convert(place1[0], place1[1])
	coor2 = convert(place2[0], place2[1])
	currentCoords = [coor1, coor2]

	if (currentCoords[0] != prevCoords[0] || currentCoords[1] != prevCoords[1]):
		print(currentCoords)
		prevCoords = currentCoords

