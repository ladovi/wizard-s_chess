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
                        pos = text
                        print ("Se escucho a1")                              
                elif text == "a2":
                        pos = text
                        print ("Se escucho a2")                                
                elif text == "a3":
                        pos = text
                        print ("Se escucho a3")
                elif text == "a4":
                        pos = text
                        print ("Se escucho a4")                                
                elif text == "a5":
                        pos = text
                        print ("Se escucho a5")    
                elif text == "a6":
                        pos = text
                        print ("Se escucho a6")                                
                elif text == "a7":
                        pos = text
                        print ("Se escucho a7")
                elif text == "a8":
                        pos = text
                        print ("Se escucho a8")    
                elif text == "b1":
                        pos = text
                        print ("Se escucho b1")                              
                elif text == "b2":
                        pos = text
                        print ("Se escucho b2")                                
                elif text == "b3":
                        pos = text
                        print ("Se escucho b3")
                elif text == "b4":
                        pos = text
                        print ("Se escucho b4")                                
                elif text == "b5":
                        pos = text
                        print ("Se escucho b5")    
                elif text == "b6" or text == "V6":
                        pos = "b6"
                        print ("Se escucho b6")                                
                elif text == "b7":
                        pos = text
                        print ("Se escucho b7")
                elif text == "b8":
                        pos = text
                        print ("Se escucho b8") 
                elif text == "c1":
                        pos = text
                        print ("Se escucho c1")                              
                elif text == "c2":
                        pos = text
                        print ("Se escucho c2")                                
                elif text == "c3":
                        pos = text
                        print ("Se escucho c3")
                elif text == "c4":
                        pos = text
                        print ("Se escucho c4")                                
                elif text == "c5":
                        pos = text
                        print ("Se escucho c5")    
                elif text == "c6":
                        pos = text
                        print ("Se escucho c6")                                
                elif text == "c7":
                        pos = text
                        print ("Se escucho c7")
                elif text == "c8":
                        pos = text
                        print ("Se escucho c8")          
                elif text == "d1":
                        pos = text
                        print ("Se escucho d1")                              
                elif text == "d2":
                        pos = text
                        print ("Se escucho d2")                                
                elif text == "d3":
                        pos = text
                        print ("Se escucho d3")
                elif text == "d4":
                        pos = text
                        print ("Se escucho d4")                                
                elif text == "d5":
                        pos = text
                        print ("Se escucho d5")    
                elif text == "d6":
                        pos = text
                        print ("Se escucho d6")                                
                elif text == "d7":
                        pos = text
                        print ("Se escucho d7")
                elif text == "d8":
                        pos = text
                        print ("Se escucho d8") 
                elif text == "e1":
                        pos = text
                        print ("Se escucho e1")                              
                elif text == "e2":
                        pos = text
                        print ("Se escucho e2")                                
                elif text == "e3":
                        pos = text
                        print ("Se escucho e3")
                elif text == "e4":
                        pos = text
                        print ("Se escucho e4")                                
                elif text == "e5":
                        pos = text
                        print ("Se escucho e5")    
                elif text == "e6":
                        pos = text
                        print ("Se escucho e6")                                
                elif text == "e7":
                        pos = text
                        print ("Se escucho e7")
                elif text == "e8":
                        pos = text
                        print ("Se escucho e8")   
                elif text == "f1":
                        pos = text
                        print ("Se escucho f1")                              
                elif text == "f2":
                        pos = text
                        print ("Se escucho f2")                                
                elif text == "f3":
                        pos = text
                        print ("Se escucho f3")
                elif text == "f4":
                        pos = text
                        print ("Se escucho f4")                                
                elif text == "f5":
                        pos = text
                        print ("Se escucho f5")    
                elif text == "f6":
                        pos = text
                        print ("Se escucho f6")                                
                elif text == "f7":
                        pos = text
                        print ("Se escucho f7")
                elif text == "f8":
                        pos = text
                        print ("Se escucho f8") 
                elif text == "g1":
                        pos = text
                        print ("Se escucho g1")                              
                elif text == "g2":
                        pos = text
                        print ("Se escucho g2")                                
                elif text == "g3":
                        pos = text
                        print ("Se escucho g3")
                elif text == "g4":
                        pos = text
                        print ("Se escucho g4")                                
                elif text == "g5":
                        pos = text
                        print ("Se escucho g5")    
                elif text == "g6":
                        pos = text
                        print ("Se escucho g6")                                
                elif text == "g7":
                        pos = text
                        print ("Se escucho g7")
                elif text == "g8":
                        pos = text
                        print ("Se escucho g8")   
                elif text == "h1":
                        pos = text
                        print ("Se escucho h1")                              
                elif text == "h2":
                        pos = text
                        print ("Se escucho h2")                                
                elif text == "h3":
                        pos = text
                        print ("Se escucho h3")
                elif text == "h4":
                        pos = text
                        print ("Se escucho h4")                                
                elif text == "h5":
                        pos = text
                        print ("Se escucho h5")    
                elif text == "h6":
                        pos = text
                        print ("Se escucho h6")                                
                elif text == "h7":
                        pos = text
                        print ("Se escucho h7")
                elif text == "h8":
                        pos = text
                        print ("Se escucho h8")
                else: 
                        funcion()                                               
                                                                                                                
        except:
                print('No se detecto nada')
                funcion()
        else: funcion()        
 
  
     


funcion()
              