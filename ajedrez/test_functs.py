import functs as f

#inp = input("enter coordenate between comas")
#coord = [int(inp[0]), int(inp[2])]
#modCoord = f.convert_btw_lines(coord[0], coord[1])
#print(modCoord)

inCoord1 = input("enter coordenate 1 between comas")
tCoord1 = [int(inCoord1[0]), int(inCoord1[2])]
inCoord2 = input("enter coordenate 2 between comas")
tCoord2 = [int(inCoord2[0]), int(inCoord2[2])]

tipo = f.determinate_type(tCoord1, tCoord2)
print("move type:",tipo)



moves = f.make_path(tCoord1, tCoord2)
print(moves)
