

from tkinter.messagebox import NO
from Eltoken import token
from contenedor import contenedor
from boton import boton
from cAreaTexto import cAreaTexto
from cClave import cClave
from check import check
from cTexto import cTexto
from etiqueta import etiqueta
from radioboton import radioboton
from tokentype import tokentype
from errores import erroR


class analSitac():

    def __init__(self,tokens) -> None:
        self.tokens = tokens
        self.tokens.append(token(tokentype.final,"#",0,0))
        self.pos=0
        self.errores =[]
        self.final= False
        self.etiquetas=[]
        self.botones=[]
        self.checks=[]
        self.radiobotones=[]
        self.cTextos=[]
        self.cAreaTextos=[]
        self.cClaves=[]
        self.contenedores=[]
        #self.body= contenedor("this",0,0,[255,255,255])
        
        # self.txt =""
        # self.title=""
        # self.titleColor=""
        # self.titleTam=""
        # self.descColor=""
        # self.descTam=""
        # self.conColor=""
        # self.conTam=""
        # self.expresiones=[]
        # self.numeros=[]
        # self.tnumeros=[]
        # self.Operaciones=[]
        # self.contOp=0

   
        self.Entrada()
        pass

    def match(self,tipo):
        if self.tokens[self.pos].type == tipo:
            
            self.pos+=1
            return

        if self.tokens[self.pos].type == tokentype.final:
            print("Fin analisis sintactico")
            self.final=True
            return

        #self.errores+= self.tokens[self.pos].lexema+" |Error, se esperaba un token"+ str(tipo)+" en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna) + "\n"
        self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba "+ tipo.name,"Sintaxis invalida"))
        self.final=True
        self.pos+=1

    def Entrada(self):
        if self.tokens[self.pos].type == tokentype.final:
            return 0

        if self.tokens[self.pos].type == tokentype.menor:
            if self.tokens[self.pos+1].type == tokentype.admiracion:
                if self.tokens[self.pos+2].type == tokentype.guion:
                    if self.tokens[self.pos+3].type == tokentype.guion:
                        if self.tokens[self.pos+4].type == tokentype.PalabraReservada:

                            if self.tokens[self.pos+4].lexema == "Controles":
                                self.CONTROLES()
                                self.Entrada()
                                pass
                            elif self.tokens[self.pos+4].lexema == "propiedades":
                                self.PROPIEDADES()
                                self.Entrada()
                                pass
                            elif self.tokens[self.pos+4].lexema == "Colocacion":
                                self.COLOCACION()
                                self.Entrada()
                                pass
                            else:
                                self.errores.append(erroR(self.tokens[self.pos+4].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba una palabra reservada válida","Sintaxis invalida"))
                                self.final=True

                        else:
                            self.errores.append(erroR(self.tokens[self.pos+4].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba una Palabra Reservada","sintaxis invalida"))
                            self.final=True
                    else:
                        self.errores.append(erroR(self.tokens[self.pos+3].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba una un guion","Sintaxis invalida"))
                        self.final=True
                else:
                    self.errores.append(erroR(self.tokens[self.pos+2].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba un guion","Sintaxis invalida"))
                    self.final=True
            else:
                self.errores.append(erroR(self.tokens[self.pos+1].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba un !","sintaxis invalida"))
                self.final=True
        else:
            self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos+4].columna,self.tokens[self.pos+4].fila,"Se esperaba un menor","sintaxis invalida"))
            self.final=True                
        
    


        # if self.tokens[self.pos].type == tokentype.menor:


        #     if self.tokens[self.pos+1].type == tokentype.letras:
        #         if self.tokens[self.pos+1].lexema == "Tipo":
        #             #print("EL DEBUGUER ES UNA SEVERENDA CHOTA")
        #             self.Tipo()
        #             self.Entrada()
        #             #Mandar a tipo
        #             pass
        #         elif self.tokens[self.pos+1].lexema == "Texto":
                    
        #             self.Texto()
        #             self.Entrada()
        #             #Mandar a Texto
        #             pass
        #         elif self.tokens[self.pos+1].lexema == "Estilo":
        #             #print("Parece que va bien")
        #             #print(self.title)
        #             self.Estilo()
        #             self.Entrada()
        #             #Mandar a Estilo
        #             pass
        #         elif self.tokens[self.pos+1].lexema == "Funcion":
        #             #print("Parece que va bien")
        #             #print(self.txt)
        #             self.Funcion()
        #             self.Entrada()
        #             #Mandar a Funcion
        #             pass
        #     else:
        #         #self.errores+=self.tokens[self.pos+1].lexema+" |Error, se esperaba un token Letras en la fila " +str(self.tokens[self.pos+1].fila)+ " y columna " + str(self.tokens[self.pos+1].columna)+ "\n"
        #         pass

        # else:
        #     pass
        #     #self.errores+= self.tokens[self.pos].lexema+" |Error, se esperaba un token < en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"

    def CONTROLES(self):
        if self.final:
            return None
        self.match(tokentype.menor)
        self.match(tokentype.admiracion)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.PalabraReservada)
        self.DEFINICION()
        self.match(tokentype.PalabraReservada)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.mayor)

    def DEFINICION(self):
        if self.final:
            return None
        if self.tokens[self.pos].lexema =="Controles":
            return None

        if self.tokens[self.pos].lexema =="Contenedor":
            self.contenedores.append(contenedor(self.tokens[self.pos+1].lexema,100,25,[255,255,255]))
            #crear contenedor
            pass
        elif self.tokens[self.pos].lexema =="Etiqueta":
            self.etiquetas.append(etiqueta(self.tokens[self.pos+1].lexema,[0,0,0],"",[0,0,0]))
            #crear etiqueta
            pass
        elif self.tokens[self.pos].lexema =="Boton":
            self.botones.append(boton(self.tokens[self.pos+1].lexema,"","Izquierda"))
            #crear Boton
            pass
        elif self.tokens[self.pos].lexema =="Check":
            self.checks.append(check(self.tokens[self.pos+1].lexema,"",False,"defaultC"))
            #crear Check
            pass
        elif self.tokens[self.pos].lexema =="RadioBoton":
            self.radiobotones.append(radioboton(self.tokens[self.pos+1].lexema,"",False,"defaultR"))
            #crear RadioBoton
            pass
        elif self.tokens[self.pos].lexema =="Texto":
            self.cTextos.append(cTexto(self.tokens[self.pos+1].lexema,"","Izquierda"))
            #crear ctexto
            pass
        elif self.tokens[self.pos].lexema =="AreaTexto":
            self.cAreaTextos.append(cAreaTexto(self.tokens[self.pos+1].lexema,""))
            #crear AreaTexto
            pass
        elif self.tokens[self.pos].lexema =="Clave":
            self.cClaves.append(cClave(self.tokens[self.pos+1].lexema,"","Izquierda"))
            #crear cClave
            pass



        self.match(tokentype.PalabraReservada)
        self.match(tokentype.id)
        self.match(tokentype.puntoComa)
        self.DEFINICION()
        

    def PROPIEDADES(self):
        if self.final:
            return None
        self.match(tokentype.menor)
        self.match(tokentype.admiracion)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.PalabraReservada)
        self.INSTRUCCION()
        self.match(tokentype.PalabraReservada)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.mayor)

    def INSTRUCCION(self):
        if self.final:
            return None
        if self.tokens[self.pos].lexema =="propiedades" or self.tokens[self.pos].lexema =="Colocacion":
            return None
        elif self.tokens[self.pos].type == tokentype.PalabraReservada:
            id=self.tokens[self.pos].lexema
            self.match(tokentype.PalabraReservada)
            self.match(tokentype.punto)
            funcion=self.tokens[self.pos].lexema
            self.match(tokentype.PalabraReservada)
            self.match(tokentype.parAbre)
            self.realizarInstruccion(id,funcion)
            self.VALORES()
            self.match(tokentype.parCierra)
            self.match(tokentype.puntoComa)
            self.INSTRUCCION()
        else:
            id=self.tokens[self.pos].lexema
            self.match(tokentype.id)
            self.match(tokentype.punto)
            funcion=self.tokens[self.pos].lexema
            self.match(tokentype.PalabraReservada)
            self.match(tokentype.parAbre)
            self.realizarInstruccion(id,funcion)
            self.VALORES()
            self.match(tokentype.parCierra)
            self.match(tokentype.puntoComa)
            self.INSTRUCCION()

    def VALORES(self):
        if self.final:
            return None
        self.VALOR()
        self.REPETIR()
        pass

    def VALOR(self):
        if self.final:
            return None
        if self.tokens[self.pos].type == tokentype.cadena:
            self.match(tokentype.cadena)
        elif self.tokens[self.pos].type == tokentype.natural:
            self.match(tokentype.natural)
        elif self.tokens[self.pos].type == tokentype.PalabraReservada:
            self.match(tokentype.PalabraReservada)
        elif self.tokens[self.pos].type == tokentype.id:
            self.match(tokentype.id)
        else:
            self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un numero,cadena,id o palabra reservada","sintaxis invalida"))
            self.final=True

    def REPETIR(self):
        if self.final:
            return None
        if self.tokens[self.pos].type == tokentype.coma:
            self.match(tokentype.coma)
            self.VALOR()
            self.REPETIR()
        
    def COLOCACION(self):
        if self.final:
            return None
        self.match(tokentype.menor)
        self.match(tokentype.admiracion)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.PalabraReservada)
        self.INSTRUCCION()
        self.match(tokentype.PalabraReservada)
        self.match(tokentype.guion)
        self.match(tokentype.guion)
        self.match(tokentype.mayor)


    def realizarInstruccion(self,id,funcion):
        if funcion == "setColorLetra":
            valores=[]
            if self.tokens[self.pos].type == tokentype.natural and self.tokens[self.pos+2].type == tokentype.natural and self.tokens[self.pos+4].type == tokentype.natural:
                valores.append(int(self.tokens[self.pos].lexema))
                valores.append(int(self.tokens[self.pos+2].lexema))
                valores.append(int(self.tokens[self.pos+4].lexema))
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for eti in self.etiquetas:
                if id == eti.id:
                    eti.colorLetra = valores
                    return None
                
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))

            
        elif funcion == "setTexto":
            valor=""
            if self.tokens[self.pos].type == tokentype.cadena:
                valor = self.tokens[self.pos].lexema
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None
            
            for eti in self.etiquetas:
                if id == eti.id:
                    eti.texto = valor
                    return None

            for obj in self.botones:
                if id == obj.id:
                    obj.texto = valor
                    return None
            
            for obj in self.checks:
                if id == obj.id:
                    obj.texto = valor
                    return None
                
            for obj in self.radiobotones:
                if id == obj.id:
                    obj.texto = valor
                    return None

            for obj in self.cTextos:
                if id == obj.id:
                    obj.texto = valor
                    return None

            for obj in self.cAreaTextos:
                if id == obj.id:
                    obj.texto = valor
                    return None

            for obj in self.cClaves:
                if id == obj.id:
                    obj.texto = valor
                    return None

            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            return None
            
        elif funcion == "setAlineacion":
            valor=""
            if self.tokens[self.pos].lexema == "Izquierdo" or self.tokens[self.pos].lexema == "Centro" or self.tokens[self.pos].lexema == "Derecho":
                valor = self.tokens[self.pos].lexema
                pass
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None
                

            for obj in self.botones:
                if id == obj.id:
                    obj.alineacion = valor
                    return None

            for obj in self.cTextos:
                if id == obj.id:
                    obj.alineacion = valor
                    return None

            for obj in self.cClaves:
                if id == obj.id:
                    obj.alineacion = valor
                    return None
            
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            return None
        elif funcion == "setColorFondo":
            valores=[]
            if self.tokens[self.pos].type == tokentype.natural and self.tokens[self.pos+2].type == tokentype.natural and self.tokens[self.pos+4].type == tokentype.natural:
                valores.append(int(self.tokens[self.pos].lexema))
                valores.append(int(self.tokens[self.pos+2].lexema))
                valores.append(int(self.tokens[self.pos+4].lexema))
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for obj in self.etiquetas:
                if id == obj.id:
                    obj.colorFondo = valores
                    return None

            for obj in self.contenedores:
                if id == obj.id:
                    obj.colorFondo = valores
                    return None
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            
            return None
        elif funcion == "setMarcada":
            valor=""
            if self.tokens[self.pos].lexema == "true":
                valor = True
                pass
            elif self.tokens[self.pos].lexema == "false":
                valor = False
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for obj in self.checks:
                if id == obj.id:
                    obj.marcada = valor
                    return None

            for obj in self.radiobotones:
                if id == obj.id:
                    obj.marcada = valor
                    return None
                
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            
            
            return None
        elif funcion == "setGrupo":
            valor =""
            if self.tokens[self.pos].type == tokentype.id:
                valor = self.tokens[self.pos].lexema
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None
            
            for obj in self.checks:
                if id == obj.id:
                    obj.grupo = valor
                    return None

            for obj in self.radiobotones:
                if id == obj.id:
                    obj.grupo = valor
                    return None
                
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            


            return None
        elif funcion == "setAncho":
            valor =100
            if self.tokens[self.pos].type == tokentype.natural:
                valor = int(self.tokens[self.pos].lexema)
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for obj in self.etiquetas:
                if id == obj.id:
                    obj.ancho = valor
                    return None

            for obj in self.contenedores:
                if id == obj.id:
                    obj.ancho = valor
                    return None
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            
            
            return None
        elif funcion == "setAlto":
            valor=25
             
            if self.tokens[self.pos].type == tokentype.natural:
                valor = int(self.tokens[self.pos].lexema)
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for obj in self.etiquetas:
                if id == obj.id:
                    obj.ancho = valor
                    return None
                    
            for obj in self.contenedores:
                if id == obj.id:
                    obj.aalto = valor
                    return None
            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))
            
            return None
        elif funcion == "add":

            return None
        elif funcion == "setPosicion":
            valorx=0
            valory=0
            if self.tokens[self.pos].type == tokentype.natural and self.tokens[self.pos+2].type == tokentype.natural:
                valorx= int(self.tokens[self.pos].lexema)
                valory=int(self.tokens[self.pos+2].lexema)
                
            else:
                self.errores.append(erroR(self.tokens[self.pos].lexema,self.tokens[self.pos].columna,self.tokens[self.pos].fila,"Se esperaba un valor Válido","Error Semántico"))
                return None

            for obj in self.etiquetas:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None

            for obj in self.botones:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None
            
            for obj in self.checks:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None
                
            for obj in self.radiobotones:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None

            for obj in self.cTextos:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None

            for obj in self.cAreaTextos:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None

            for obj in self.cClaves:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None

            for obj in self.contenedores:
                if id == obj.id:
                    obj.x = valorx
                    obj.y = valory
                    return None


            self.errores.append(erroR(self.tokens[self.pos-3].lexema,self.tokens[self.pos-3].columna,self.tokens[self.pos-3].fila,"Se esperaba una id válida","Error Sintactico"))   
            return None

        pass



    # def Tipo(self):
    #     self.match(tokentype.menor)
        
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.Operacion()
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Operacion(self):
        

    #     if self.tokens[self.pos].type == tokentype.menor:
    #         if self.tokens[self.pos+1].type == tokentype.letras:
    #             if self.tokens[self.pos+1].lexema == "Numero":
    #                 self.Numero()
    #                 self.Operacion()
    #                 #Mandar a Numero
    #                 pass
    #             elif self.tokens[self.pos+1].lexema == "Operacion":
    #                 #Mandar a ver cual operacion es
    #                 if self.tokens[self.pos+2].type == tokentype.igual:
    #                     if self.tokens[self.pos+3].type == tokentype.letras:
    #                         if self.tokens[self.pos+3].lexema == "SUMA":
    #                             self.expresiones.append("SUMA")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1+n2
    #                             t_resultado="("+tn1+"+"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)
                                
    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "RESTA":
    #                             self.expresiones.append("RESTA")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1-n2
    #                             t_resultado="("+tn1+"-"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "MULTIPLICACION":
    #                             self.expresiones.append("MULTIPLICACION")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1*n2
    #                             t_resultado="("+tn1+"*"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)
    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "DIVISION":
    #                             self.expresiones.append("DIVISION")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1/n2
    #                             t_resultado="("+tn1+"/"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)


    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "RAIZ":
    #                             self.expresiones.append("RAIZ")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n2**(1/n1)
    #                             t_resultado="("+tn2+"^(1/"+tn1+"))"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)


    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "POTENCIA":
    #                             self.expresiones.append("POTENCIA")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1**n2
    #                             t_resultado="("+tn1+"^"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "INVERSO":
    #                             self.expresiones.append("INVERSO")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)
        
                                
    #                             n1=self.numeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1**(-1)
    #                             t_resultado="("+tn1+"^(-1))"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "SENO":
    #                             self.expresiones.append("SENO")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n1=self.numeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=math.sin(n1)
    #                             t_resultado="(sen("+tn1+"))"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "COSENO":
    #                             self.expresiones.append("COSENO")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n1=self.numeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=math.cos(n1)
    #                             t_resultado="(cos("+tn1+"))"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)


    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "TANGENTE":
    #                             self.expresiones.append("TANGENTE")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n1=self.numeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=math.tan(n1)
    #                             t_resultado="(tan("+tn1+"))"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         elif self.tokens[self.pos+3].lexema == "MOD":
    #                             self.expresiones.append("MOD")
    #                             self.contOp+=1
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.igual)
    #                             self.match(tokentype.letras)
    #                             self.match(tokentype.mayor)
    #                             self.Operacion()
    #                             self.match(tokentype.menor)
    #                             self.match(tokentype.slash)
    #                             if self.tokens[self.pos].lexema =="Operacion":
    #                                 self.match(tokentype.letras)
    #                             else:
    #                                 self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #                             #ESPERAR QUE VENGA EL SLASG, Y SINO; ERROR
    #                             self.match(tokentype.mayor)

    #                             n2=self.numeros.pop()
    #                             n1=self.numeros.pop()
    #                             tn2=self.tnumeros.pop()
    #                             tn1=self.tnumeros.pop()
    #                             resultado=n1%n2
    #                             t_resultado="("+tn1+"%"+tn2+")"
    #                             self.contOp-=1
    #                             if len(self.numeros)==0 and self.contOp==0:
                                
    #                                 self.Operaciones.append([resultado,t_resultado])
    #                             else:
    #                                 self.numeros.append(resultado)
    #                                 self.tnumeros.append(t_resultado)

    #                             self.expresiones.append("Result")
    #                             self.Operacion()
    #                             #Agregar arbol o algo para hacer las operaciones
    #                             pass
    #                         else:
    #                             self.errores+=self.tokens[self.pos+3].lexema+" |Error, se esperaba una palabra reservada en la fila " +str(self.tokens[self.pos+3].fila)+ " y columna " + str(self.tokens[self.pos+3].columna)+"\n"
    #                     else:
    #                         self.errores+=self.tokens[self.pos+3].lexema+" |Error, se esperaba un token Letras en la fila " +str(self.tokens[self.pos+3].fila)+ " y columna " + str(self.tokens[self.pos+3].columna)+"\n"
    #                 else:
    #                     self.errores+=self.tokens[self.pos+2].lexema+" |Error, se esperaba un token Igual en la fila " +str(self.tokens[self.pos+2].fila)+ " y columna " + str(self.tokens[self.pos+2].columna)+"\n"
    #                 pass
    #             else:
    #                 #self.errores+=self.tokens[i+1].lexema+" |Error, se esperaba la palabra reservada Operacion en la fila " +str(self.tokens[i+1].fila)+ " y columna " + str(self.tokens[i+1].columna)+"\n"
    #                 pass
    #         else:
    #             #self.errores+=self.tokens[i+1].lexema+" |Error, se esperaba un token Letras o slash en la fila " +str(self.tokens[i+1].fila)+ " y columna " + str(self.tokens[i+1].columna)+"\n"
    #             pass

    #     else:
    #         self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba un token < en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #     pass
                
    # def Numero(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     if self.tokens[self.pos].type == tokentype.numero:
    #         self.expresiones.append(int(self.tokens[self.pos].lexema))
    #         self.numeros.append(int(self.tokens[self.pos].lexema))
    #         self.tnumeros.append(self.tokens[self.pos].lexema)
    #         self.match(tokentype.numero)
            
            
    #     elif self.tokens[self.pos].type == tokentype.decimal:
    #         self.expresiones.append(float(self.tokens[self.pos].lexema))
    #         self.numeros.append(float(self.tokens[self.pos].lexema))
    #         self.tnumeros.append(self.tokens[self.pos].lexema)
    #         self.match(tokentype.decimal)
    #     else:
    #         self.errores+=self.tokens[self.pos].lexema+" |Error, se esperaba un token Igual en la fila " +str(self.tokens[self.pos].fila)+ " y columna " + str(self.tokens[self.pos].columna)+"\n"
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
        
    # def Texto(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.Parrafo()
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Parrafo(self):
    #     if self.tokens[self.pos].type == tokentype.letras:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.letras)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.decimal:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.decimal)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.numero:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.numero)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.mayor:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.mayor)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.cadena:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.cadena)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.igual:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.igual)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.slash:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.slash)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.corcheteAbre:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.corcheteAbre)
    #         self.Parrafo()
    #     elif self.tokens[self.pos].type == tokentype.corcheteCierre:
    #         self.txt+= self.tokens[self.pos].lexema
    #         self.txt+=" "
    #         self.match(tokentype.corcheteCierre)
    #         self.Parrafo()
           
            
    # def Funcion(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.Etiqueta()
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Etiqueta(self):
    #     if self.tokens[self.pos].type == tokentype.menor:
    #         if self.tokens[self.pos+1].type == tokentype.letras:
    #             if self.tokens[self.pos+1].lexema == "Titulo":
    #                 self.Titulo()
    #                 self.Etiqueta()
    #                 pass
    #             elif self.tokens[self.pos+1].lexema == "Descripcion":
    #                 self.Descripcion()
    #                 self.Etiqueta()
    #                 pass
    #             elif self.tokens[self.pos+1].lexema == "Contenido":
    #                 self.Contenido()
    #                 self.Etiqueta()
    #                 pass
    
    # def Titulo(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     if self.tokens[self.pos].type == tokentype.letras:
    #         self.title = self.tokens[self.pos].lexema
    #         self.match(tokentype.letras)
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    
    # def Descripcion(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.match(tokentype.corcheteAbre)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.corcheteCierre)
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Contenido(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.match(tokentype.corcheteAbre)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.corcheteCierre)
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Estilo(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)
    #     self.Parametro()
    #     self.match(tokentype.menor)
    #     self.match(tokentype.slash)
    #     self.match(tokentype.letras)
    #     self.match(tokentype.mayor)

    # def Parametro(self):
    #     if self.tokens[self.pos].type == tokentype.menor:
    #         if self.tokens[self.pos+1].type == tokentype.letras:
    #             if self.tokens[self.pos+1].lexema == "Titulo":
    #                 self.TituloPara()
    #                 self.Parametro()
    #                 pass
    #             elif self.tokens[self.pos+1].lexema == "Descripcion":
    #                 self.DescripcionPara()
    #                 self.Parametro()
    #                 pass
    #             elif self.tokens[self.pos+1].lexema == "Contenido":
    #                 self.ContenidoPara()
    #                 self.Parametro()
    #                 pass

    # def TituloPara(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.letras:
    #         self.titleColor = self.tokens[self.pos].lexema
    #         self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.numero:
    #         self.titleTam = self.tokens[self.pos].lexema
    #         self.match(tokentype.numero)
        
    #     self.match(tokentype.slash)
    #     self.match(tokentype.mayor)
    #     #print("Titulo--------------")
    #     #print(self.titleColor)
    #     #print(self.titleTam)

    # def DescripcionPara(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.letras:
    #         self.descColor = self.tokens[self.pos].lexema
    #         self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.numero:
    #         self.descTam = self.tokens[self.pos].lexema
    #         self.match(tokentype.numero)
        
    #     self.match(tokentype.slash)
    #     self.match(tokentype.mayor)
    #     #print("Descripcion--------------")
    #     #print(self.descColor)
    #     #print(self.descTam)

    # def ContenidoPara(self):
    #     self.match(tokentype.menor)
    #     self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.letras:
    #         self.conColor = self.tokens[self.pos].lexema
    #         self.match(tokentype.letras)

    #     self.match(tokentype.letras)
    #     self.match(tokentype.igual)
    #     if self.tokens[self.pos].type == tokentype.numero:
    #         self.conTam = self.tokens[self.pos].lexema
    #         self.match(tokentype.numero)
        
    #     self.match(tokentype.slash)
    #     self.match(tokentype.mayor)
    #     #print("Contenido--------------")
    #     #print(self.conColor)
    #     #print(self.conTam)



        
                