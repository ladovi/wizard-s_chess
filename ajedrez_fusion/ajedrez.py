import functs as f
import numpy as np
import speech_recognition as sr

A = np.array([["Tn", "Cn", "An", "rn", "Rn", "An", "Cn", "Tn"], 
              ["Pn1", "Pn1", "Pn1", "x", "Pn1", "Pn1", "Pn1", "Pn1"], 
              ["x", "x", "x", "x", "x", "x", "x", "x"], 
              ["x", "x", "x", "x", "x", "x", "x", "x"],
              ["x", "x", "x", "x", "x", "x", "x", "x"],
              ["x", "x", "x", "x", "x", "x", "x", "x"],
              ["Pb1", "Pb1", "Pb1", "Pb1", "Pb1", "Pb1", "Pb1", "Pb1"],
              ["Tb", "Cb", "Ab", "rb", "Rb", "Ab", "Cb", "Tb"]])

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]



def pos1(): 
        global pos
        pos = 'algo'
        r = sr.Recognizer()  
        with sr.Microphone() as source:
                print("Diga un comando")
                audio = r.listen(source)

        try:
                text = r.recognize_google(audio, language="es-AR")
                print(text)
                if text == "a1":
                        pos = "A1"
                        print ("Se escucho a1")                              
                elif text == "a2":
                        pos = "A2"
                        print ("Se escucho a2")                                
                elif text == "a3" or text == "A3":
                        pos = "A3"
                        print ("Se escucho a3")
                elif text == "a4" or text == "A4":
                        pos = "A4"
                        print ("Se escucho a4")                                
                elif text == "a5":
                        pos = "A5"
                        print ("Se escucho a5")    
                elif text == "a6" or text == "A6":
                        pos = "A6"
                        print ("Se escucho a6")                                
                elif text == "a7":
                        pos = "A7"
                        print ("Se escucho a7")
                elif text == "a8":
                        pos = "A8"
                        print ("Se escucho a8")    
                elif text == "b1":
                        pos = "B1"
                        print ("Se escucho b1")                              
                elif text == "b2":
                        pos = "B2"
                        print ("Se escucho b2")                                
                elif text == "b3" or text == "B3":
                        pos = "B3"
                        print ("Se escucho b3")
                elif text == "b4":
                        pos = "B4"
                        print ("Se escucho b4")                                
                elif text == "b5":
                        pos = "B5"
                        print ("Se escucho b5")    
                elif text == "b6" or text == "V6":
                        pos = "B6"
                        print ("Se escucho b6")                                
                elif text == "b7":
                        pos = "B7"
                        print ("Se escucho b7")
                elif text == "b8" or text =="v8":
                        pos = "B8"
                        print ("Se escucho b8") 
                elif text == "c1":
                        pos = "C1"
                        print ("Se escucho c1")                              
                elif text == "c2" or text =="C2":
                        pos = "C2"
                        print ("Se escucho c2")                                
                elif text == "c3" or text == "C3":
                        pos = "C3"
                        print ("Se escucho c3")
                elif text == "c4":
                        pos = "C4"
                        print ("Se escucho c4")                                
                elif text == "c5":
                        pos = "C5"
                        print ("Se escucho c5")    
                elif text == "c6":
                        pos = "C6"
                        print ("Se escucho c6")                                
                elif text == "c7":
                        pos = "C7"
                        print ("Se escucho c7")
                elif text == "c8":
                        pos = "C8"
                        print ("Se escucho c8")          
                elif text == "d1":
                        pos = "D1"
                        print ("Se escucho d1")                              
                elif text == "d2"or text == "dedos":
                        pos = "D2"
                        print ("Se escucho d2")                                
                elif text == "d3" or text == "D3":
                        pos = "D3"
                        print ("Se escucho d3")
                elif text == "d4":
                        pos = "D4"
                        print ("Se escucho d4")                                
                elif text == "d5" or text == "de 5":
                        pos = "D5"
                        print ("Se escucho d5")    
                elif text == "d6":
                        pos = "D6"
                        print ("Se escucho d6")                                
                elif text == "d7":
                        pos = "D7"
                        print ("Se escucho d7")
                elif text == "d8":
                        pos = "D8"
                        print ("Se escucho d8") 
                elif text == "e1":
                        pos = "E1"
                        print ("Se escucho e1")                              
                elif text == "e2" or text == "E2":
                        pos = "E2"
                        print ("Se escucho e2")                                
                elif text == "e3":
                        pos = "E3"
                        print ("Se escucho e3")
                elif text == "e4":
                        pos = "E4"
                        print ("Se escucho e4")                                
                elif text == "e5" or text == "E5":
                        pos = "E5"
                        print ("Se escucho e5")    
                elif text == "e6" or text == "es6":
                        pos = "E6"
                        print ("Se escucho e6")                                
                elif text == "e7":
                        pos = "E7"
                        print ("Se escucho e7")
                elif text == "e8" or text == "y8":
                        pos = "E8"
                        print ("Se escucho e8")   
                elif text == "f1":
                        pos = "F1"
                        print ("Se escucho f1")                              
                elif text == "f2":
                        pos = "F2"
                        print ("Se escucho f2")                                
                elif text == "f3":
                        pos = "F3"
                        print ("Se escucho f3")
                elif text == "f4" or text == "F4":
                        pos = "F4"
                        print ("Se escucho f4")                                
                elif text == "f5":
                        pos = "F5"
                        print ("Se escucho f5")    
                elif text == "f6":
                        pos = "F6"
                        print ("Se escucho f6")                                
                elif text == "f7" or text =="F7":
                        pos = "F7"
                        print ("Se escucho f7")
                elif text == "f8":
                        pos = "F8"
                        print ("Se escucho f8") 
                elif text == "g1":
                        pos = "G1"
                        print ("Se escucho g1")                              
                elif text == "g2" or text =="G2":
                        pos = "G2"
                        print ("Se escucho g2")                                
                elif text == "g3" or text == "G3":
                        pos = "G3"
                        print ("Se escucho g3")
                elif text == "g4":
                        pos = "G4"
                        print ("Se escucho g4")                                
                elif text == "g5":
                        pos = "G5"
                        print ("Se escucho g5")    
                elif text == "g6" or text == "G6":
                        pos = "G6"
                        print ("Se escucho g6")                                
                elif text == "g7":
                        pos = "G7"
                        print ("Se escucho g7")
                elif text == "g8":
                        pos = "G8"
                        print ("Se escucho g8")   
                elif text == "h1":
                        pos = "H1"
                        print ("Se escucho h1")                              
                elif text == "h2":
                        pos = "H2"
                        print ("Se escucho h2")                                
                elif text == "h3":
                        pos = "H3"
                        print ("Se escucho h3")
                elif text == "h4":
                        pos = "H4"
                        print ("Se escucho h4")                                
                elif text == "h5":
                        pos = "H5"
                        print ("Se escucho h5")    
                elif text == "h6":
                        pos = "H6"
                        print ("Se escucho h6")                                
                elif text == "h7":
                        pos = "H7"
                        print ("Se escucho h7")
                elif text == "h8":
                        pos = "H8"
                        print ("Se escucho h8")
                else: 
                        funcion()                                               
                                                                                                                
        except:
                print('No se detecto nada')
                pos1()



def pos2(): 
        global posf
        posf = 'algo'
        r = sr.Recognizer()  
        with sr.Microphone() as source:
                print("Diga a donde mover")
                audio = r.listen(source)

        try:
                text = r.recognize_google(audio, language="es-AR")
                print(text)
                if text == "a1":
                        posf = "A1"
                        print ("Se escucho a1")                              
                elif text == "a2":
                        posf = "A2"
                        print ("Se escucho a2")                                
                elif text == "a3" or text == "A3":
                        posf = "A3"
                        print ("Se escucho a3")
                elif text == "a4" or text == "A4":
                        posf = "A4"
                        print ("Se escucho a4")                                
                elif text == "a5":
                        posf = "A5"
                        print ("Se escucho a5")    
                elif text == "a6" or text == "A6":
                        posf = "A6"
                        print ("Se escucho a6")                                
                elif text == "a7":
                        posf = "A7"
                        print ("Se escucho a7")
                elif text == "a8":
                        posf = "A8"
                        print(posf)
                        print ("Se escucho a8")    
                elif text == "b1":
                        posf = "B1"
                        print ("Se escucho b1")                              
                elif text == "b2":
                        posf = "B2"
                        print ("Se escucho b2")                                
                elif text == "b3" or text == "B3":
                        posf = "B3"
                        print ("Se escucho b3")
                elif text == "b4":
                        posf = "B4"
                        print ("Se escucho b4")                                
                elif text == "b5":
                        posf = "B5"
                        print ("Se escucho b5")    
                elif text == "b6" or text == "V6":
                        posf = "B6"
                        print ("Se escucho b6")                                
                elif text == "b7":
                        posf = "B7"
                        print ("Se escucho b7")
                elif text == "b8" or text =="v8":
                        posf = "B8"
                        print ("Se escucho b8") 
                elif text == "c1":
                        posf = "C1"
                        print ("Se escucho c1")                              
                elif text == "c2" or text =="C2":
                        posf = "C2"
                        print ("Se escucho c2")                                
                elif text == "c3" or text == "C3":
                        posf = "C3"
                        print ("Se escucho c3")
                elif text == "c4":
                        posf = "C4"
                        print ("Se escucho c4")                                
                elif text == "c5":
                        posf = "C5"
                        print ("Se escucho c5")    
                elif text == "c6":
                        posf = "C6"
                        print ("Se escucho c6")                                
                elif text == "c7":
                        posf = "C7"
                        print ("Se escucho c7")
                elif text == "c8":
                        posf = "C8"
                        print ("Se escucho c8")          
                elif text == "d1":
                        posf = "D1"
                        print ("Se escucho d1")                              
                elif text == "d2" or text == "dedos":
                        posf = "D2"
                        print ("Se escucho d2")                                
                elif text == "d3" or text == "D3":
                        posf = "D3"
                        print ("Se escucho d3")
                elif text == "d4":
                        posf = "D4"
                        print ("Se escucho d4")                                
                elif text == "d5" or text == "de 5":
                        posf = "D5"
                        print ("Se escucho d5")    
                elif text == "d6":
                        posf = "D6"
                        print ("Se escucho d6")                                
                elif text == "d7":
                        posf = "D7"
                        print ("Se escucho d7")
                elif text == "d8":
                        posf = "D8"
                        print ("Se escucho d8") 
                elif text == "e1":
                        posf = "E1"
                        print ("Se escucho e1")                              
                elif text == "e2" or text == "E2":
                        posf = "E2"
                        print ("Se escucho e2")                                
                elif text == "e3":
                        posf = "E3"
                        print ("Se escucho e3")
                elif text == "e4":
                        posf = "E4"
                        print ("Se escucho e4")                                
                elif text == "e5" or text == "E5":
                        posf = "E5"
                        print ("Se escucho e5")    
                elif text == "e6" or text == "es6":
                        posf = "E6"
                        print ("Se escucho e6")                                
                elif text == "e7":
                        posf = "E7"
                        print ("Se escucho e7")
                elif text == "e8" or text == "y8":
                        posf = "E8"
                        print ("Se escucho e8")   
                elif text == "f1":
                        posf = "F1"
                        print ("Se escucho f1")                              
                elif text == "f2":
                        posf = "F2"
                        print ("Se escucho f2")                                
                elif text == "f3":
                        posf = "F3"
                        print ("Se escucho f3")
                elif text == "f4" or text == "F4":
                        posf = "F4"
                        print ("Se escucho f4")                                
                elif text == "f5":
                        posf = "F5"
                        print ("Se escucho f5")    
                elif text == "f6":
                        posf = "F6"
                        print ("Se escucho f6")                                
                elif text == "f7" or text =="F7":
                        posf = "F7"
                        print ("Se escucho f7")
                elif text == "f8":
                        posf = "F8"
                        print ("Se escucho f8") 
                elif text == "g1":
                        posf = "G1"
                        print ("Se escucho g1")                              
                elif text == "g2" or text =="G2":
                        posf = "G2"
                        print ("Se escucho g2")                                
                elif text == "g3" or text == "G3":
                        posf = "G3"
                        print ("Se escucho g3")
                elif text == "g4":
                        posf = "G4"
                        print ("Se escucho g4")                                
                elif text == "g5":
                        posf = "G5"
                        print ("Se escucho g5")    
                elif text == "g6" or text == "G6":
                        posf = "G6"
                        print ("Se escucho g6")                                
                elif text == "g7":
                        posf = "G7"
                        print ("Se escucho g7")
                elif text == "g8":
                        posf = "G8"
                        print ("Se escucho g8")   
                elif text == "h1":
                        posf = "H1"
                        print ("Se escucho h1")                              
                elif text == "h2":
                        posf = "H2"
                        print ("Se escucho h2")                                
                elif text == "h3":
                        posf = "H3"
                        print ("Se escucho h3")
                elif text == "h4":
                        posf = "H4"
                        print ("Se escucho h4")                                
                elif text == "h5":
                        posf = "H5"
                        print ("Se escucho h5")    
                elif text == "h6":
                        posf = "H6"
                        print ("Se escucho h6")                                
                elif text == "h7":
                        posf = "H7"
                        print ("Se escucho h7")
                elif text == "h8":
                        posf = "H8"
                        print ("Se escucho h8")
                else:
                        posfinal()                      
                                                                                                                
        except:
                print('No se detecto nada')
                pos2()


def mov_builder(): 
    global X1 
    global Y1
    global X2
    global Y2
    for i in range(len(letters)): 
        if mov[0] == letters[i]:
            Y1 = i
        if mov2[0] == letters[i]:
            Y2 = i

    X1 = -(int(mov[1]) - 8)
    X2 = -(int(mov2[1]) - 8)

    print("X1 = " + str(X1))
    print("Y1 = " + str(Y1))
    print("X2 = " + str(X2))
    print("Y2 = " + str(Y2))
    print('Letra primer movimiento = ' + A[X1, Y1]) #printea letra que corresponde al movimiento
    print('Letra primer movimiento = ' + A[X2, Y2])



def piece_finder():
    if(A[X1, Y1] == "Tb"):
        print("Movimiento: Torre (Color: Blanco)")
        torre()
    if(A[X1, Y1] == "Cb"):
        print("Movimiento: Caballo (Color: Blanco)")
        caballo()
    if(A[X1, Y1] == "Ab"):
        print("Movimiento: Alfil (Color: Blanco)")
        alfil()
    if(A[X1, Y1] == "rb"):
        print("Movimiento: Rey (Color: Blanco)")
        rey()
    if(A[X1, Y1] == "Rb"):
        print("Movimiento: Reina (Color: Blanco)")
        reina()
    if(A[X1, Y1] == "Pb1"):
        print("Movimiento: Peon (Color: Blanco)")
        peon()
    elif(A[X1, Y1] == "Pb2"):
        print("Movimiento: Peon (Color: Blanco, Pb2)")
        peon()
    if(A[X1, Y1] == "x"):
        print("No hay ninguna pieza en esa posicion")
    
    if(A[X1, Y1] == "Tn"):
        print("Movimiento: Torre(Color: Negro)")
        torre()
    if(A[X1, Y1] == "Cn"):
        print("Movimiento: Caballo (Color: Negro)")
        caballo()
    if(A[X1, Y1] == "An"):
        print("Movimiento: Alfil (Color: Negro)")
        alfil()
    if(A[X1, Y1] == "rn"):
        print("Movimiento: Rey (Color: Negro)")
        rey()
    if(A[X1, Y1] == "Rn"):
        print("Movimiento: Reina (Color: Negro)")
        reina()
    if(A[X1, Y1] == "Pn1"):
        print("Movimiento: Peon (Color: Negro)")
        peon()
    elif(A[X1, Y1] == "Pn2"):
        print("Movimiento: Peon (Color: Negro, Pn2) ")
        peon()
    if(A[X1, Y1] == "xn"):
        print("No hay ninguna pieza en posicion")
        
def begin_move():
    if(A[X1, Y1] == "x"):
        print("No hay una pieza en ese lugar")
    else:
        A[X2, Y2] = A[X1, Y1]
        A[X1, Y1] = "x"
        cord1 = [X1, Y1]
        cord2 = [X2, Y2]
        f.funcion_maxima(cord1, cord2)
       #print(A)

def peon():
    print('Funcion Peon:')
    noValido = False
    x = A[X1, Y1]
    y = A[X2, Y2]
    c = A[X2 - 1, Y2]
    print(x, y, c)
    print(X2 - X1)
    print(Y2 - Y1)
    if(-(X2 - X1) == 2 and (Y2 - Y1) == 0): #  movimiento doble
        print('holaaa')
        if(x[2] == '1'):
            if(x[1] == 'n'):
                A[X1, Y1] = 'Pn2'
            else:
                A[X1, Y1] = 'Pb2'
            noValido = True
        elif(c == 'x'):
            print('aqui')
            noValido = True
        else:
            print('aqui nomas')
            noValido = False

    if(noValido == False):
        if((X2 - X1) == 2 and (Y2 - Y1) == 0): #  movimiento doble
            print('adiosss')
            if(x[2] == '1'):
                if(x[1] == 'n'):
                    A[X1, Y1] = 'Pn2'
                else:
                    A[X1, Y1] = 'Pb2'
                noValido = True
            elif(c == 'x'):
                print('aqui we')
                noValido = True
            else:
                print('aqui nomas we')
                noValido = False
                
    if((X2 - X1) == 1 and (Y2 - Y1) == 0): #  movimiento normal
        print('1111111111')
        if(y == 'x'):
            noValido = True
        else:
            noValido = False
        
    if((X2 - X1) == 1 and (Y2 - Y1) == 1): #  movimiento para comer
        print('2222222222')
        if(y[1] == "n"):
            noValido = True
        elif(y[1] == "b"):
            noValido = True
    
    if(noValido == True):
        try:
            if(x[1] == y[1]):
                noValido = False
            else:
                print('che aca esta el problema ')
                noValido = True
        except:
            print('qwertyu')
            noValido = True
    
    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')
    
def torre():
    print('Funcion Torre:')
    x = A[X1, Y1]
    y = A[X2, Y2]
    z = (X2 - X1) - 1
    i = 1
    noValido = False

    print(X2 - X1)
    if((X2 - X1) > 0 and (Y2 - Y1) == 0): # movimiento vertical
        noValido = True

    elif((X2 - X1) == 0 and (Y2 - Y1) > 0): # movimiento horizontal
        noValido = True

    else:
        print('---->> Movimiento no valido')
        noValido = False
        
    while(i <= z): # revisa posiciones entre X1 y X2
        m = X1 + i 
        c = A[m, Y1]
        try:
            if(c[1] == 'n'):
                if(x[1] == 'n'):
                    noValido = False
                else:
                    noValido = True
            elif(c[1] == 'b'):
                if(x[1] == 'b'):
                    noValido = False
                else:
                    noValido = True
            else:
                noValido = False
        except:
            noValido = False
            
        try:
            if(c == 'x'):
                noValido = True
        except:
            pass
        i += 1
    if(noValido == True):
        try:
            if(y == 'x'):
                noValido = True
            elif(y[1] == 'n'):
                if(x[1] == 'n'):
                    noValido = False
                else:
                    noValido = True
            elif(y[1] == 'b'):
                if(x[1] == 'b'):
                    noValido = False
                else:
                    noValido = True
            else:
                noValido = False
        except:
            noValido = False
    else:
        noValido = False
    
    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')
        
def caballo():
    print('Funcion Caballo:')
    noValido = False
    x = A[X1, Y1]
    y = A[X2, Y2]
    
    if((X2 - X1) == 2 and (Y2 - Y1) == 1): #  movimiento 1
        noValido = True
    elif((X2 - X1) == 1 and (Y2 - Y1) == 2): #  movimiento 2
        noValido = True
    else:
        noValido = False
        
    try: #  revisa si hay pieza del mismo color
        if(y == 'x'):
            noValido = True
        elif(y[1] == 'n'):
            if(x[1] == 'n'):
                noValido = False
            else:
                noValido = True
        elif(y[1] == 'b'):
            if(x[1] == 'b'):
                noValido = False
            else:
                noValido = True
        else:
            noValido = False
    except:
        noValido = False
        
    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')
            
def alfil():
    print('Funcion Alfil:')
    noValido = False
    x = A[X1, Y1]
    y = A[X2, Y2]
    z = +(X2 - X1)
    i = 1
    print((X2 - X1), -(Y2 - Y1))
    print(z)
    if((X2 - X1) ** 2 == (Y2 - Y1) ** 2):
        noValido = True
    else:
        noValido = False
    
    if(noValido == True):
        while(i <= z): # revisa posiciones entre X1 y X2
            m = X1
            n = Y1
            
            if((X2 - X1) > 0 and (Y2 - Y1) > 0):
                m += 1
                n += 1
            elif((X2 - X1) < 0 and (Y2 - Y1) < 0):
                m -= 1
                n -= 1
            elif((X2 - X1) < 0 and (Y2 - Y1) > 0):
                m -= 1
                n += 1
            else:
                m += 1
                n -= 1
                                
            
            c = A[m, n]
            print(m, n, c)
            
            try:
                if(c[1] == 'n'):
                    noValido = False
                if(c[1] == 'b'):
                    noValido = False
            except:
                pass
            
            i += 1
    
    if(noValido == True):
        try: #  revisa si hay pieza del mismo color
            if(y == 'x'):
                noValido = True
            elif(y[1] == 'n'):
                if(x[1] == 'n'):
                    noValido = False
                else:
                    noValido = True
            elif(y[1] == 'b'):
                if(x[1] == 'b'):
                    noValido = False
                else:
                    noValido = True
            else:
                noValido = False
        except:
            noValido = False
    
    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')

def rey(): 
    print('Funcion Rey:')
    noValido = False    
    y = A[X2, Y2]
    x = A[X1, Y1]

    print(X2 - X1)  
    print(Y2 - Y1)  

    if((X2 - X1) == 1 and (Y2 - Y1) == 0): #  movimiento normal
        noValido = True  
    elif((X2 - X1) == -1 and (Y2 - Y1) == 0): #  movimiento normal
        noValido = True                  
    elif((X2 - X1) == 0 and (Y2 - Y1) == 1): #  movimiento normal
        noValido = True 
    elif((X2 - X1) == 0 and (Y2 - Y1) == -1): #  movimiento normal
        noValido = True  
    elif((X2 - X1) == 1 and (Y2 - Y1) == 1): #  movimiento para comer
        noValido = True
    elif((X2 - X1) == -1 and (Y2 - Y1) == -1): #  movimiento para comer
        noValido = True
    elif((X2 - X1) == -1 and (Y2 - Y1) == 1): #  movimiento para comer
        noValido = True
    elif((X2 - X1) == 1 and (Y2 - Y1) == -1): #  movimiento para comer
        noValido = True
    else:
        noValido = False
    
    if(noValido == True):
        try:
            if(y == 'x'):
                noValido = True
            elif(y[1] == 'n'):
                if(x[1] == 'n'):
                    noValido = False
            elif(y[1] == 'b'):
                if(x[1] == 'b'):
                    noValido = False
            else:
                noValido = True
        except:
            noValido = True
    
    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')

def reina():
    print('Funcion Reina:')
    x = A[X1, Y1]
    y = A[X2, Y2]
    z = (X2 - X1) - 1
    i = 1
    noValido = False
    var = True

    if(z == -1):
        print('aca nomas brooooo')
        z = (Y2 - Y1) - 1

    j = +(X2 - X1)
    p = 1

    if((X2 - X1) ** 2 == (Y2 - Y1) ** 2):
        var = True
        noValido = True
    else:
        var = False
        noValido = False

    if(var == False):
        print('holavariaaaaa')
        if((X2 - X1) > 0 and (Y2 - Y1) == 0): # movimiento vertical
            noValido = False
        elif((X2 - X1) == 0 and (Y2 - Y1) > 0): # movimiento horizontal
            noValido = False
        else:
            noValido = True

    if(var == False):
        while(i <= z): # revisa posiciones entre X1 y X2
            m = X1 + i 
            c = A[m, Y1]
            try:
                if(c[1] == 'n'):
                    if(x[1] == 'n'):
                        noValido = False
                    else:
                        noValido = True
                elif(c[1] == 'b'):
                    if(x[1] == 'b'):
                        noValido = False
                    else:
                        noValido = True
                else:
                    noValido = False
            except:
                noValido = False
                
            try:
                if(c == 'x'):
                    noValido = True
            except:
                pass
            i += 1
    
    if(var == True):
        while(p <= j): # revisa posiciones entre X1 y X2
            m = X1
            n = Y1
            
            if((X2 - X1) > 0 and (Y2 - Y1) > 0):
                m += 1
                n += 1
            elif((X2 - X1) < 0 and (Y2 - Y1) < 0):
                m -= 1
                n -= 1
            elif((X2 - X1) < 0 and (Y2 - Y1) > 0):
                m -= 1
                n += 1
            else:
                m += 1
                n -= 1
                                
            
            c = A[m, n]
            print(m, n, c)
            print(noValido)
            try:
                if(c[1] == 'n'):
                    noValido = False
                if(c[1] == 'b'):
                    noValido = False
            except:
                pass
            
            p += 1
    
    if(noValido == True):
        try: #  revisa si hay pieza del mismo color
            if(y == 'x'):
                noValido = True
            elif(y[1] == 'n'):
                if(x[1] == 'n'):
                    noValido = False
                else:
                    noValido = True
            elif(y[1] == 'b'):
                if(x[1] == 'b'):
                    noValido = False
                else:
                    noValido = True
            else:
                noValido = False
        except:
            noValido = False

    if(noValido == True):
        print('---->> Movimiento valido')
        begin_move()
    else:
        print('---->> Movimiento no valido')

while True:
    print(A)
    pos1()
    pos2()
    mov = pos        #input('Pieza a mover:')
    mov2 = posf      #input('Lugar a mover:')
    mov_builder()
    print(X1, Y1, X2, Y2)
    piece_finder()


#print(A[X1, Y1])
