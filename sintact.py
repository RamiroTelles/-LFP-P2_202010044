from Eltoken import token
from tokentype import tokentype
from errores import erroR
import math

class analSitac():

    def __init__(self,tokens) -> None:
        self.tokens = tokens
        self.tokens.append(token(tokentype.final,"#",0,0))
        self.pos=0
        self.errores =[]
        self.txt =""
        self.title=""
        self.titleColor=""
        self.titleTam=""
        self.descColor=""
        self.descTam=""
        self.conColor=""
        self.conTam=""
        self.expresiones=[]
        self.numeros=[]
        self.tnumeros=[]
        self.Operaciones=[]
        self.contOp=0

   
        self.Entrada()
        pass

    def match(self,tipo):
        if self.tokens[self.pos].type == tipo:
            
            self.pos+=1
            return

        if self.tokens[self.pos].type == tokentype.final:
            print("Fin analisis sintactico")
            return

        self.errores+= self.tokens[self.pos].lexema+" |Error, se esperaba un token"+ str(tipo)+" en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna) + "\n"
        self.pos+=1

    def Entrada(self):
        

        if self.tokens[self.pos].type == tokentype.menor:


            if self.tokens[self.pos+1].type == tokentype.letras:
                if self.tokens[self.pos+1].lexema == "Tipo":
                    #print("EL DEBUGUER ES UNA SEVERENDA CHOTA")
                    self.Tipo()
                    self.Entrada()
                    #Mandar a tipo
                    pass
                elif self.tokens[self.pos+1].lexema == "Texto":
                    
                    self.Texto()
                    self.Entrada()
                    #Mandar a Texto
                    pass
                elif self.tokens[self.pos+1].lexema == "Estilo":
                    #print("Parece que va bien")
                    #print(self.title)
                    self.Estilo()
                    self.Entrada()
                    #Mandar a Estilo
                    pass
                elif self.tokens[self.pos+1].lexema == "Funcion":
                    #print("Parece que va bien")
                    #print(self.txt)
                    self.Funcion()
                    self.Entrada()
                    #Mandar a Funcion
                    pass
            else:
                #self.errores+=self.tokens[self.pos+1].lexema+" |Error, se esperaba un token Letras en la fila " +str(self.tokens[self.pos+1].fila)+ " y columna " + str(self.tokens[self.pos+1].columna)+ "\n"
                pass

        else:
            pass
            #self.errores+= self.tokens[self.pos].lexema+" |Error, se esperaba un token < en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"


    def Tipo(self):
        self.match(tokentype.menor)
        
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.Operacion()
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Operacion(self):
        

        if self.tokens[self.pos].type == tokentype.menor:
            if self.tokens[self.pos+1].type == tokentype.letras:
                if self.tokens[self.pos+1].lexema == "Numero":
                    self.Numero()
                    self.Operacion()
                    #Mandar a Numero
                    pass
                elif self.tokens[self.pos+1].lexema == "Operacion":
                    #Mandar a ver cual operacion es
                    if self.tokens[self.pos+2].type == tokentype.igual:
                        if self.tokens[self.pos+3].type == tokentype.letras:
                            if self.tokens[self.pos+3].lexema == "SUMA":
                                self.expresiones.append("SUMA")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1+n2
                                t_resultado="("+tn1+"+"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)
                                
                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "RESTA":
                                self.expresiones.append("RESTA")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1-n2
                                t_resultado="("+tn1+"-"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "MULTIPLICACION":
                                self.expresiones.append("MULTIPLICACION")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1*n2
                                t_resultado="("+tn1+"*"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)
                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "DIVISION":
                                self.expresiones.append("DIVISION")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1/n2
                                t_resultado="("+tn1+"/"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)


                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "RAIZ":
                                self.expresiones.append("RAIZ")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n2**(1/n1)
                                t_resultado="("+tn2+"^(1/"+tn1+"))"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)


                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "POTENCIA":
                                self.expresiones.append("POTENCIA")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1**n2
                                t_resultado="("+tn1+"^"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "INVERSO":
                                self.expresiones.append("INVERSO")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)
        
                                
                                n1=self.numeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1**(-1)
                                t_resultado="("+tn1+"^(-1))"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "SENO":
                                self.expresiones.append("SENO")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n1=self.numeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=math.sin(n1)
                                t_resultado="(sen("+tn1+"))"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "COSENO":
                                self.expresiones.append("COSENO")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n1=self.numeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=math.cos(n1)
                                t_resultado="(cos("+tn1+"))"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)


                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "TANGENTE":
                                self.expresiones.append("TANGENTE")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n1=self.numeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=math.tan(n1)
                                t_resultado="(tan("+tn1+"))"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            elif self.tokens[self.pos+3].lexema == "MOD":
                                self.expresiones.append("MOD")
                                self.contOp+=1
                                self.match(tokentype.menor)
                                self.match(tokentype.letras)
                                self.match(tokentype.igual)
                                self.match(tokentype.letras)
                                self.match(tokentype.mayor)
                                self.Operacion()
                                self.match(tokentype.menor)
                                self.match(tokentype.slash)
                                if self.tokens[self.pos].lexema =="Operacion":
                                    self.match(tokentype.letras)
                                else:
                                    self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
                                #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
                                self.match(tokentype.mayor)

                                n2=self.numeros.pop()
                                n1=self.numeros.pop()
                                tn2=self.tnumeros.pop()
                                tn1=self.tnumeros.pop()
                                resultado=n1%n2
                                t_resultado="("+tn1+"%"+tn2+")"
                                self.contOp-=1
                                if len(self.numeros)==0 and self.contOp==0:
                                
                                    self.Operaciones.append([resultado,t_resultado])
                                else:
                                    self.numeros.append(resultado)
                                    self.tnumeros.append(t_resultado)

                                self.expresiones.append("Result")
                                self.Operacion()
                                #Agregar arbol o algo para hacer las operaciones
                                pass
                            else:
                                self.errores+=self.tokens[self.pos+3].lexema+" |Error, se esperaba una palabra reservada en la fila " +str(self.tokens[self.pos+3].fila)+ " y columna " + str(self.tokens[self.pos+3].columna)+"\n"
                        else:
                            self.errores+=self.tokens[self.pos+3].lexema+" |Error, se esperaba un token Letras en la fila " +str(self.tokens[self.pos+3].fila)+ " y columna " + str(self.tokens[self.pos+3].columna)+"\n"
                    else:
                        self.errores+=self.tokens[self.pos+2].lexema+" |Error, se esperaba un token Igual en la fila " +str(self.tokens[self.pos+2].fila)+ " y columna " + str(self.tokens[self.pos+2].columna)+"\n"
                    pass
                else:
                    #self.errores+=self.tokens[i+1].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[i+1].fila)+ " y columna " + str(self.tokens[i+1].columna)+"\n"
                    pass
            else:
                #self.errores+=self.tokens[i+1].lexema+" |Error, se esperaba un token Letras o slash en la fila " +str(self.tokens[i+1].fila)+ " y columna " + str(self.tokens[i+1].columna)+"\n"
                pass

        else:
            self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba un token < en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
        pass
                
    def Numero(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        if self.tokens[self.pos].type == tokentype.numero:
            self.expresiones.append(int(self.tokens[self.pos].lexema))
            self.numeros.append(int(self.tokens[self.pos].lexema))
            self.tnumeros.append(self.tokens[self.pos].lexema)
            self.match(tokentype.numero)
            
            
        elif self.tokens[self.pos].type == tokentype.decimal:
            self.expresiones.append(float(self.tokens[self.pos].lexema))
            self.numeros.append(float(self.tokens[self.pos].lexema))
            self.tnumeros.append(self.tokens[self.pos].lexema)
            self.match(tokentype.decimal)
        else:
            self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba un token Igual en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        
    def Texto(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.Parrafo()
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Parrafo(self):
        if self.tokens[self.pos].type == tokentype.letras:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.letras)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.decimal:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.decimal)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.numero:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.numero)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.mayor:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.mayor)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.cadena:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.cadena)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.igual:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.igual)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.slash:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.slash)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.corcheteAbre:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.corcheteAbre)
            self.Parrafo()
        elif self.tokens[self.pos].type == tokentype.corcheteCierre:
            self.txt+= self.tokens[self.pos].lexema
            self.txt+=" "
            self.match(tokentype.corcheteCierre)
            self.Parrafo()
           
            
    def Funcion(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.igual)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.Etiqueta()
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Etiqueta(self):
        if self.tokens[self.pos].type == tokentype.menor:
            if self.tokens[self.pos+1].type == tokentype.letras:
                if self.tokens[self.pos+1].lexema == "Titulo":
                    self.Titulo()
                    self.Etiqueta()
                    pass
                elif self.tokens[self.pos+1].lexema == "Descripcion":
                    self.Descripcion()
                    self.Etiqueta()
                    pass
                elif self.tokens[self.pos+1].lexema == "Contenido":
                    self.Contenido()
                    self.Etiqueta()
                    pass
    
    def Titulo(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        if self.tokens[self.pos].type == tokentype.letras:
            self.title = self.tokens[self.pos].lexema
            self.match(tokentype.letras)
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
    
    def Descripcion(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.match(tokentype.corcheteAbre)
        self.match(tokentype.letras)
        self.match(tokentype.corcheteCierre)
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Contenido(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.match(tokentype.corcheteAbre)
        self.match(tokentype.letras)
        self.match(tokentype.corcheteCierre)
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Estilo(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)
        self.Parametro()
        self.match(tokentype.menor)
        self.match(tokentype.slash)
        self.match(tokentype.letras)
        self.match(tokentype.mayor)

    def Parametro(self):
        if self.tokens[self.pos].type == tokentype.menor:
            if self.tokens[self.pos+1].type == tokentype.letras:
                if self.tokens[self.pos+1].lexema == "Titulo":
                    self.TituloPara()
                    self.Parametro()
                    pass
                elif self.tokens[self.pos+1].lexema == "Descripcion":
                    self.DescripcionPara()
                    self.Parametro()
                    pass
                elif self.tokens[self.pos+1].lexema == "Contenido":
                    self.ContenidoPara()
                    self.Parametro()
                    pass

    def TituloPara(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.letras:
            self.titleColor = self.tokens[self.pos].lexema
            self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.numero:
            self.titleTam = self.tokens[self.pos].lexema
            self.match(tokentype.numero)
        
        self.match(tokentype.slash)
        self.match(tokentype.mayor)
        #print("Titulo--------------")
        #print(self.titleColor)
        #print(self.titleTam)

    def DescripcionPara(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.letras:
            self.descColor = self.tokens[self.pos].lexema
            self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.numero:
            self.descTam = self.tokens[self.pos].lexema
            self.match(tokentype.numero)
        
        self.match(tokentype.slash)
        self.match(tokentype.mayor)
        #print("Descripcion--------------")
        #print(self.descColor)
        #print(self.descTam)

    def ContenidoPara(self):
        self.match(tokentype.menor)
        self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.letras:
            self.conColor = self.tokens[self.pos].lexema
            self.match(tokentype.letras)

        self.match(tokentype.letras)
        self.match(tokentype.igual)
        if self.tokens[self.pos].type == tokentype.numero:
            self.conTam = self.tokens[self.pos].lexema
            self.match(tokentype.numero)
        
        self.match(tokentype.slash)
        self.match(tokentype.mayor)
        #print("Contenido--------------")
        #print(self.conColor)
        #print(self.conTam)



        
                