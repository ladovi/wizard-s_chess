import speech_recognition as sr
pos = "algo"
posf = "algoo"

def funcion(): 
        r = sr.Recognizer()  
        with sr.Microphone() as source:
                print("Diga un comando")
                audio = r.listen(source)

        try:
                text = r.recognize_google(audio, language="es-AR")
                print(text)
                if text == "a1":
                        pos = "a1"
                        print ("Se escucho a1")                              
                elif text == "a2":
                        pos = "a2"
                        print ("Se escucho a2")                                
                elif text == "a3" or text == "A3":
                        pos = "a3"
                        print ("Se escucho a3")
                elif text == "a4" or text == "A4":
                        pos = "a4"
                        print ("Se escucho a4")                                
                elif text == "a5":
                        pos = "a5"
                        print ("Se escucho a5")    
                elif text == "a6" or text == "A6":
                        pos = "a6"
                        print ("Se escucho a6")                                
                elif text == "a7":
                        pos = "a7"
                        print ("Se escucho a7")
                elif text == "a8":
                        pos = "a8"
                        print ("Se escucho a8")    
                elif text == "b1":
                        pos = "b1"
                        print ("Se escucho b1")                              
                elif text == "b2":
                        pos = "b2"
                        print ("Se escucho b2")                                
                elif text == "b3" or text == "B3":
                        pos = "b3"
                        print ("Se escucho b3")
                elif text == "b4":
                        pos = "b4"
                        print ("Se escucho b4")                                
                elif text == "b5":
                        pos = "b5"
                        print ("Se escucho b5")    
                elif text == "b6" or text == "V6":
                        pos = "b6"
                        print ("Se escucho b6")                                
                elif text == "b7":
                        pos = "b7"
                        print ("Se escucho b7")
                elif text == "b8" or text =="v8":
                        pos = "b8"
                        print ("Se escucho b8") 
                elif text == "c1":
                        pos = "c1"
                        print ("Se escucho c1")                              
                elif text == "c2" or text =="C2":
                        pos = "c2"
                        print ("Se escucho c2")                                
                elif text == "c3" or text == "C3":
                        pos = "c3"
                        print ("Se escucho c3")
                elif text == "c4":
                        pos = "c4"
                        print ("Se escucho c4")                                
                elif text == "c5":
                        pos = "c5"
                        print ("Se escucho c5")    
                elif text == "c6":
                        pos = "c6"
                        print ("Se escucho c6")                                
                elif text == "c7":
                        pos = "c7"
                        print ("Se escucho c7")
                elif text == "c8":
                        pos = "c8"
                        print ("Se escucho c8")          
                elif text == "d1":
                        pos = "d1"
                        print ("Se escucho d1")                              
                elif text == "d2"or text == "dedos":
                        pos = "d2"
                        print ("Se escucho d2")                                
                elif text == "d3" or text == "D3":
                        pos = "d3"
                        print ("Se escucho d3")
                elif text == "d4":
                        pos = "d4"
                        print ("Se escucho d4")                                
                elif text == "d5" or text == "de 5":
                        pos = "d5"
                        print ("Se escucho d5")    
                elif text == "d6":
                        pos = "d6"
                        print ("Se escucho d6")                                
                elif text == "d7":
                        pos = "d7"
                        print ("Se escucho d7")
                elif text == "d8":
                        pos = "d8"
                        print ("Se escucho d8") 
                elif text == "e1":
                        pos = "e1"
                        print ("Se escucho e1")                              
                elif text == "e2" or text == "E2":
                        pos = "e2"
                        print ("Se escucho e2")                                
                elif text == "e3":
                        pos = "e3"
                        print ("Se escucho e3")
                elif text == "e4":
                        pos = "e4"
                        print ("Se escucho e4")                                
                elif text == "e5" or text == "E5":
                        pos = "e5"
                        print ("Se escucho e5")    
                elif text == "e6" or text == "es6":
                        pos = "e6"
                        print ("Se escucho e6")                                
                elif text == "e7":
                        pos = "e7"
                        print ("Se escucho e7")
                elif text == "e8" or text == "y8":
                        pos = "e8"
                        print ("Se escucho e8")   
                elif text == "f1":
                        pos = "f1"
                        print ("Se escucho f1")                              
                elif text == "f2":
                        pos = "f2"
                        print ("Se escucho f2")                                
                elif text == "f3":
                        pos = "f3"
                        print ("Se escucho f3")
                elif text == "f4" or text == "F4":
                        pos = "f4"
                        print ("Se escucho f4")                                
                elif text == "f5":
                        pos = "f5"
                        print ("Se escucho f5")    
                elif text == "f6":
                        pos = "f6"
                        print ("Se escucho f6")                                
                elif text == "f7" or text =="F7":
                        pos = "f7"
                        print ("Se escucho f7")
                elif text == "f8":
                        pos = "f8"
                        print ("Se escucho f8") 
                elif text == "g1":
                        pos = "g1"
                        print ("Se escucho g1")                              
                elif text == "g2" or text =="G2":
                        pos = "g2"
                        print ("Se escucho g2")                                
                elif text == "g3" or text == "G3":
                        pos = "g3"
                        print ("Se escucho g3")
                elif text == "g4":
                        pos = "g4"
                        print ("Se escucho g4")                                
                elif text == "g5":
                        pos = "g5"
                        print ("Se escucho g5")    
                elif text == "g6" or text == "G6":
                        pos = "g6"
                        print ("Se escucho g6")                                
                elif text == "g7":
                        pos = "g7"
                        print ("Se escucho g7")
                elif text == "g8":
                        pos = "g8"
                        print ("Se escucho g8")   
                elif text == "h1":
                        pos = "h1"
                        print ("Se escucho h1")                              
                elif text == "h2":
                        pos = "h2"
                        print ("Se escucho h2")                                
                elif text == "h3":
                        pos = "h3"
                        print ("Se escucho h3")
                elif text == "h4":
                        pos = "h4"
                        print ("Se escucho h4")                                
                elif text == "h5":
                        pos = "h5"
                        print ("Se escucho h5")    
                elif text == "h6":
                        pos = "h6"
                        print ("Se escucho h6")                                
                elif text == "h7":
                        pos = "h7"
                        print ("Se escucho h7")
                elif text == "h8":
                        pos = "h8"
                        print ("Se escucho h8")
                else: 
                        funcion()                                               
                                                                                                                
        except:
                print('No se detecto nada')
                funcion()
     



 
        
def posfinal(): 
        r = sr.Recognizer()  
        with sr.Microphone() as source:
                print("Diga a donde mover")
                audio = r.listen(source)

        try:
                text = r.recognize_google(audio, language="es-AR")
                print(text)
                if text == "a1":
                        posf = "a1"
                        print ("Se escucho a1")                              
                elif text == "a2":
                        posf = "a2"
                        print ("Se escucho a2")                                
                elif text == "a3" or text == "A3":
                        posf = "a3"
                        print ("Se escucho a3")
                elif text == "a4" or text == "A4":
                        posf = "a4"
                        print ("Se escucho a4")                                
                elif text == "a5":
                        posf = "a5"
                        print ("Se escucho a5")    
                elif text == "a6" or text == "A6":
                        posf = "a6"
                        print ("Se escucho a6")                                
                elif text == "a7":
                        posf = "a7"
                        print ("Se escucho a7")
                elif text == "a8":
                        posf = "a8"
                        print ("Se escucho a8")    
                elif text == "b1":
                        posf = "b1"
                        print ("Se escucho b1")                              
                elif text == "b2":
                        posf = "b2"
                        print ("Se escucho b2")                                
                elif text == "b3" or text == "B3":
                        posf = "b3"
                        print ("Se escucho b3")
                elif text == "b4":
                        posf = "b4"
                        print ("Se escucho b4")                                
                elif text == "b5":
                        posf = "b5"
                        print ("Se escucho b5")    
                elif text == "b6" or text == "V6":
                        posf = "b6"
                        print ("Se escucho b6")                                
                elif text == "b7":
                        posf = "b7"
                        print ("Se escucho b7")
                elif text == "b8" or text =="v8":
                        posf = "b8"
                        print ("Se escucho b8") 
                elif text == "c1":
                        posf = "c1"
                        print ("Se escucho c1")                              
                elif text == "c2" or text =="C2":
                        posf = "c2"
                        print ("Se escucho c2")                                
                elif text == "c3" or text == "C3":
                        posf = "c3"
                        print ("Se escucho c3")
                elif text == "c4":
                        posf = "c4"
                        print ("Se escucho c4")                                
                elif text == "c5":
                        posf = "c5"
                        print ("Se escucho c5")    
                elif text == "c6":
                        posf = "c6"
                        print ("Se escucho c6")                                
                elif text == "c7":
                        posf = "c7"
                        print ("Se escucho c7")
                elif text == "c8":
                        posf = "c8"
                        print ("Se escucho c8")          
                elif text == "d1":
                        posf = "d1"
                        print ("Se escucho d1")                              
                elif text == "d2" or text == "dedos":
                        posf = "d2"
                        print ("Se escucho d2")                                
                elif text == "d3" or text == "D3":
                        posf = "d3"
                        print ("Se escucho d3")
                elif text == "d4":
                        posf = "d4"
                        print ("Se escucho d4")                                
                elif text == "d5" or text == "de 5":
                        posf = "d5"
                        print ("Se escucho d5")    
                elif text == "d6":
                        posf = "d6"
                        print ("Se escucho d6")                                
                elif text == "d7":
                        posf = "d7"
                        print ("Se escucho d7")
                elif text == "d8":
                        posf = "d8"
                        print ("Se escucho d8") 
                elif text == "e1":
                        posf = "e1"
                        print ("Se escucho e1")                              
                elif text == "e2" or text == "E2":
                        posf = "e2"
                        print ("Se escucho e2")                                
                elif text == "e3":
                        posf = "e3"
                        print ("Se escucho e3")
                elif text == "e4":
                        posf = "e4"
                        print ("Se escucho e4")                                
                elif text == "e5" or text == "E5":
                        posf = "e5"
                        print ("Se escucho e5")    
                elif text == "e6" or text == "es6":
                        posf = "e6"
                        print ("Se escucho e6")                                
                elif text == "e7":
                        posf = "e7"
                        print ("Se escucho e7")
                elif text == "e8" or text == "y8":
                        posf = "e8"
                        print ("Se escucho e8")   
                elif text == "f1":
                        posf = "f1"
                        print ("Se escucho f1")                              
                elif text == "f2":
                        posf = "f2"
                        print ("Se escucho f2")                                
                elif text == "f3":
                        posf = "f3"
                        print ("Se escucho f3")
                elif text == "f4" or text == "F4":
                        posf = "f4"
                        print ("Se escucho f4")                                
                elif text == "f5":
                        posf = "f5"
                        print ("Se escucho f5")    
                elif text == "f6":
                        posf = "f6"
                        print ("Se escucho f6")                                
                elif text == "f7" or text =="F7":
                        posf = "f7"
                        print ("Se escucho f7")
                elif text == "f8":
                        posf = "f8"
                        print ("Se escucho f8") 
                elif text == "g1":
                        posf = "g1"
                        print ("Se escucho g1")                              
                elif text == "g2" or text =="G2":
                        posf = "g2"
                        print ("Se escucho g2")                                
                elif text == "g3" or text == "G3":
                        posf = "g3"
                        print ("Se escucho g3")
                elif text == "g4":
                        posf = "g4"
                        print ("Se escucho g4")                                
                elif text == "g5":
                        posf = "g5"
                        print ("Se escucho g5")    
                elif text == "g6" or text == "G6":
                        posf = "g6"
                        print ("Se escucho g6")                                
                elif text == "g7":
                        posf = "g7"
                        print ("Se escucho g7")
                elif text == "g8":
                        posf = "g8"
                        print ("Se escucho g8")   
                elif text == "h1":
                        posf = "h1"
                        print ("Se escucho h1")                              
                elif text == "h2":
                        posf = "h2"
                        print ("Se escucho h2")                                
                elif text == "h3":
                        posf = "h3"
                        print ("Se escucho h3")
                elif text == "h4":
                        posf = "h4"
                        print ("Se escucho h4")                                
                elif text == "h5":
                        posf = "h5"
                        print ("Se escucho h5")    
                elif text == "h6":
                        posf = "h6"
                        print ("Se escucho h6")                                
                elif text == "h7":
                        posf = "h7"
                        print ("Se escucho h7")
                elif text == "h8":
                        posf = "h8"
                        print ("Se escucho h8")
                else:
                        posfinal()                      
                                                                                                                
        except:
                print('No se detecto nada')
                posfinal()
     


funcion()
posfinal()              