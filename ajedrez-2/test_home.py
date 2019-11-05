import functs as f

inCoord1 = input("enter coordenate 1 between comas")
c1 = [int(inCoord1[0]), int(inCoord1[2])]
inCoord2 = input("enter coordenate 2 between comas")
c2 = [int(inCoord2[0]), int(inCoord2[2])]

tirita = f.funcion_maxima(c1, c2)
f.home(tirita)