
from email import message
from this import d
from tkinter import messagebox
from tkinter.messagebox import NO
#from wsgiref.validate import validator
#from pyparsing import col
from Eltoken import token
from tkinter import N, Tk
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
#from elemento import elemento
from generadorForm import generadorForm
from tokentype import tokentype
from errores import erroR

class analizador():

    def __init__(self) -> None:
        #self.resultadosOperaciones= []
        #self.expresiones = []
        
        
        #self.numOp=0
        #self.operaciones=[]
        self.abierto=""
        pass

    def analizadorLexico(self,texto):
        estado=0
        lexema=""
        columna=1
        fila=1
        errores=[]
        tokens= []
        coments=[]
        i=0
        actual=""
        long = len(texto)
        while(i<long and texto[i]!=None):
            actual=texto[i]

            if estado==0:
                if actual=="<":
                    lexema+=actual
                    
                    
                    tokens.append(token(tokentype.menor,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                if actual==">":
                    lexema+=actual
                    
                    
                    tokens.append(token(tokentype.mayor,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual==";":
                    lexema+= actual
                    tokens.append(token(tokentype.puntoComa,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="-":
                    lexema+= actual
                    tokens.append(token(tokentype.guion,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual == '!':
                    lexema+= actual
                    tokens.append(token(tokentype.admiracion,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== '(':
                    lexema+=actual
                    tokens.append(token(tokentype.parAbre,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== ')':
                    lexema+=actual
                    tokens.append(token(tokentype.parCierra,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== '.':
                    lexema+=actual
                    tokens.append(token(tokentype.punto,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== ',':
                    lexema+=actual
                    tokens.append(token(tokentype.coma,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='\"':
                    lexema+=actual
                    estado= 5
                    i+=1
                    columna+=1
                    continue
                elif actual.isalpha():
                    estado=4
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual.isdigit():
                    estado=3
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual=="/":
                    estado=6
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue

                elif actual=='\n':
                    fila+=1
                    i+=1
                    columna=1
                    continue
                elif actual=='\t' or actual=='\r':
                    i+=1
                    columna+=4
                    continue
                elif actual==" ":
                    i+=1
                    columna+=1
                    continue
                else:
                    #print("Simbolo " + actual + " no reconocido")
                    lexema+=actual
                    errores.append(erroR(lexema,columna,fila,"Se esperaba otro simbolo","Expresion invalida"))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
            elif estado==5:
                if actual=="\"":
                    lexema+=actual
                    estado=0
                    tokens.append(token(tokentype.cadena,lexema,fila,columna-len(lexema)))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="\n":
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                elif actual=="\t" or actual=="\r":
                    lexema+=actual
                    i+=1
                    columna+=4
                    continue
                else:
    
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
            elif estado==4:
                if actual.isalpha():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual.isdigit():
                    estado=8
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    if self.buscarReservada(lexema):
                        tokens.append(token(tokentype.PalabraReservada,lexema,fila,columna-len(lexema)))
                    else:
                        tokens.append(token(tokentype.id,lexema,fila,columna-len(lexema)))
                    lexema=""
                    estado=0
                    

                    #comprobar si es palabra reservada, sino guardarlo como id
                    #lexema+=actual
                    #i+=1
                    #columna+=1
                    continue
            elif estado==8:
                if actual.isalpha() or actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    tokens.append(token(tokentype.id,lexema,fila,columna-len(lexema)))
                    lexema=""
                    estado=0
                    continue
            elif estado==3:
                if actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual==".":
                    estado=7
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    estado=0
                    tokens.append(token(tokentype.natural,lexema,fila,columna-len(lexema)))
                    lexema=""
                    continue
            elif estado==7:
                if actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    estado=11
                    continue
                else:
                    errores.append(erroR(lexema,fila,columna-len(lexema),"Se esperaba un digito","Expresion invalida"))
                    lexema=""
                    estado=0
                    continue
            elif estado==11:
                if actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    tokens.append(token(tokentype.decimal,lexema,fila,columna-len(lexema)))
                    estado=0
                    lexema=""
                    continue

            elif estado ==6:
                if actual=="*":
                    estado=10
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual=="/":
                    estado=9
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores.append(erroR(lexema,fila,columna,"Se esperaba un / o *","Expresion invalida"))
                    lexema=""
                    estado=0
                    continue
            elif estado==10:
                if actual=="*":
                    estado=12
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual=="\n":
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                elif actual=="\t" or actual=='\r':
                    lexema+=actual
                    i+=1
                    columna+=4
                    
                    continue
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
            elif estado==12:
                if actual=="/":
                    lexema+=actual
                    coments.append(token(tokentype.comentarioM,lexema,fila,columna-len(lexema)))
                    lexema=""
                    i+=1
                    columna+=1
                    estado=0
                    continue
                elif actual=="\n":
                    estado=10
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                elif actual=="\t" or actual=='\r':
                    estado=10
                    lexema+=actual
                    i+=1
                    columna+=4
                    
                    continue
                else:
                    estado=10
                    lexema+=actual
                    i+=1
                    columna+=4
                    continue
            elif estado==9:
                if actual=="\t" or actual=='\r':
                    lexema+=actual
                    i+=1
                    columna+=4
                    continue
                elif actual=="\n":
                    
                    coments.append(token(tokentype.comentarioL,lexema,fila,columna-len(lexema)))
                    lexema=""
                    estado=0
                    i+=1
                    columna=1
                    fila+=1
                    continue
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue









            
        if estado==10 or estado == 12:
            errores.append(erroR(lexema,fila,columna-len(lexema),"Se esperaba un *","Expresion invalida"))
            
        resultados = []
        resultados.append(tokens)
        resultados.append(errores)
        resultados.append(coments)
        return resultados

    def cargarArchivo(self):
        Tk().withdraw()
        txt=""
        try:
            path = askopenfilename(filetypes=[('.gpw','*.gpw'),('*.*','*.*')])
            #print(path)
            self.abierto=path
            with open(path,encoding='utf-8') as file:
                txt = file.read().strip()
                file.close()
        except:
            print("Error")

        
        
        return str(txt)

    def guardar(self,txt):
        Tk().withdraw()
        if self.abierto=="":
            try:
                path = asksaveasfilename(filetypes=[('.lfp',"*.lfp"),("*.*","*.*")])
                path+=".lfp"
                print(path)
                self.abierto=path
                with open(path,'w') as file:
                    file.write(txt)
                    file.close()
                    messagebox.showinfo(message="Se ha guardado con exito",title="Guardado")
            except:
                messagebox.showerror(message="No se pudo guardar el archivo",title="Error")
        else:
            try:
                
                with open(self.abierto,'w') as file:
                    file.write(txt)
                    file.close()
                    messagebox.showinfo(message="Se ha guardado con exito",title="Guardado")
            except:
                messagebox.showerror(message="No se pudo guardar el archivo",title="Error")

    def guardarComo(self):
        self.abierto=""     



        
    
        
   
        

    def reporteTokens(self,tokens):
        i=0
        txt = '''
<html>
    <head>

    </head>
    <link rel="stylesheet" href="estilo.css">

<body>
    <div class="container">
        <table>
            <thead>
                <tr>
                    <th>Correlativo</th>
                    <th>Tipo token</th>
                    <th>Numero Token</th>
                    <th>Lexema</th>
                    
                </tr>
            </thead>
<tbody>'''
        for obj in tokens:
            txt+="<tr> "
            txt+="<th> "+ str(i) + "<th>\n"

            if obj.type == tokentype.menor:

                txt+= "<th> menor</th>\n"
            
            elif obj.type == tokentype.mayor:

                txt+= "<th> mayor</th>\n"
            elif obj.type == tokentype.puntoComa:

                txt+= "<th> puntoCOma</th>\n"
            
            elif obj.type == tokentype.guion:

                txt+= "<th> guion</th>\n"
            
            elif obj.type == tokentype.admiracion:

                txt+= "<th> admiracion</th>\n"
            elif obj.type == tokentype.parAbre:

                txt+= "<th> ParentesisAbre</th>\n"
            elif obj.type == tokentype.parCierra:

                txt+= "<th> ParentesisCierra</th>\n"
            elif obj.type == tokentype.punto:

                txt+= "<th> punto</th>\n"
            elif obj.type == tokentype.decimal:

                txt+= "<th> decimal</th>\n"  
            elif obj.type == tokentype.coma:

                txt+= "<th> coma</th>\n"
            elif obj.type == tokentype.PalabraReservada:

                txt+= "<th> PalabraReservada</th>\n" 
            elif obj.type == tokentype.id:

                txt+= "<th> id</th>\n" 
            elif obj.type == tokentype.cadena:

                txt+= "<th> cadena</th>\n" 
            elif obj.type == tokentype.natural:

                txt+= "<th> natural</th>\n" 
            elif obj.type == tokentype.comentarioL:

                txt+= "<th> comentario</th>\n" 
            elif obj.type == tokentype.comentarioM:

                txt+= "<th> comentario</th>\n"



            if obj.type == tokentype.menor:

                txt+= "<th> 1001</th>\n"
            
            elif obj.type == tokentype.mayor:

                txt+= "<th> 1002</th>\n"
            elif obj.type == tokentype.puntoComa:

                txt+= "<th> 1003</th>\n"
            
            elif obj.type == tokentype.guion:

                txt+= "<th> 1004</th>\n"
            
            elif obj.type == tokentype.admiracion:

                txt+= "<th> 1005</th>\n"
            elif obj.type == tokentype.parAbre:

                txt+= "<th> 1006</th>\n"
            elif obj.type == tokentype.parCierra:

                txt+= "<th> 1007</th>\n"
            elif obj.type == tokentype.punto:

                txt+= "<th> 1008</th>\n"
            elif obj.type == tokentype.decimal:

                txt+= "<th> 1009</th>\n"  
            elif obj.type == tokentype.coma:

                txt+= "<th> 1010</th>\n"
            elif obj.type == tokentype.PalabraReservada:

                txt+= "<th> 1011</th>\n" 
            elif obj.type == tokentype.id:

                txt+= "<th> 1012</th>\n" 
            elif obj.type == tokentype.cadena:

                txt+= "<th> 1013</th>\n" 
            elif obj.type == tokentype.natural:

                txt+= "<th> 1014</th>\n" 
            elif obj.type == tokentype.comentarioL:

                txt+= "<th> 1015</th>\n" 
            elif obj.type == tokentype.comentarioM:

                txt+= "<th> 1016</th>\n"                

            
            txt+="<th> "+ str(obj.lexema)+ "</th>\n"
           
            
            txt+="</tr>"
            i+=1
        txt+='''
            </tbody>
        </table>
</div>
    

</body>
</html>
        '''
        try:


            with open("ReporteTokens.html",'w') as file:
                file.write(txt)

                file.close()
        
        except:
            print("No se pudo generar el reporte de tokens")
        pass

    def reporteErrores(self,erroreslexicos,erroresSintacticos,erroresSemanticos):
        #filas = erroreslexicos.split('\n')
        i=0

        txt = '''
    <html>
        <head>

        </head>
        <link rel="stylesheet" href="estilo.css">

    <body>
        <div class="container">
            <table>
                <thead>
                    <tr>
                        <th>Tipo de Error</th>
                        
                        
                        <th>Fila</th>
                        <th>Columna</th>
                        <th>Valor Esperado</th>
                        <th>Descripcion</th>
                        
                        
                    </tr>
                </thead>
    <tbody>'''
        for obj in erroreslexicos:
            txt+="<tr> "
            txt+="<th> Lexico </th>\n" 
            
            txt+="<th> " + str(obj.fila)+ "</th>\n"
            txt+="<th> " + str(obj.columna)+ "</th>\n"
            txt+="<th> " + obj.esperado+ "</th>\n"
            txt+="<th> " + obj.desc+ "</th>\n"
               
            #txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"
        for obj in erroresSintacticos:

            
            txt+="<tr> "
            txt+="<th> Sintactico </th>\n"
           
        
            
            txt+="<th> " + str(obj.fila)+ "</th>\n"
            txt+="<th> " + str(obj.columna)+ "</th>\n"
            txt+="<th> " + obj.esperado+ "</th>\n"
            txt+="<th> " + obj.desc+ "</th>\n"
            

            txt+="</tr>"



        txt+= '''
            </tbody>
        </table>
       
        

            '''
        

        txt+='''
              
    </div>
        

    </body>
    </html>
            '''
        try:


            with open("ReporteErrores.html",'w') as file:
                file.write(txt)

                file.close()
            
        except:
            print("No se pudo generar el reporte de errores")



    def buscarReservada(self,lexema):
        if lexema == "Controles":
            return True
        elif lexema == "Etiqueta":
            return True
        elif lexema == "Boton":
            return True
        elif lexema == "Check":
            return True
        elif lexema == "RadioBoton":
            return True
        elif lexema == "Texto":
            return True
        elif lexema == "AreaTexto":
            return True
        elif lexema == "Clave":
            return True
        elif lexema == "Contenedor":
            return True
        elif lexema == "propiedades":
            return True
        elif lexema == "setColorLetra":
            return True
        elif lexema == "setTexto":
            return True
        elif lexema == "setAlineacion":
            return True
        elif lexema == "setColorFondo":
            return True
        elif lexema == "setMarcada":
            return True
        elif lexema == "setGrupo":
            return True
        elif lexema == "setAncho":
            return True
        elif lexema == "setAlto":
            return True
        elif lexema == "add":
            return True
        elif lexema == "Colocacion":
            return True
        elif lexema == "this":
            return True
        elif lexema == "setPosicion":
            return True
        else:
            return False

#     def generarResultados(self,titulo,t_color,t_tamaño,descripcion,d_color,d_tamaño,Operaciones,o_color,o_tamaño):
#         css=""
#         css+="h2{ \ncolor: " + self.adivinarColor(t_color) + ";\n"
#         css+="font-size: "+t_tamaño+"em;\n}\n"
#         css+="h3{ \ncolor: " + self.adivinarColor(d_color) + ";\n"
#         css+="font-size: "+d_tamaño+"em;\n}\n"
#         css+="p{ \ncolor: " + self.adivinarColor(o_color) + ";\n"
#         css+="font-size: "+o_tamaño+"em;\n}\n"
        

#         html="""
# <html>
#     <head></head>
#      <link rel="stylesheet" href="estiloDinamico.css">
# <body>\n"""
#         html+="<h2>" + titulo+"</h2>\n"
#         html+="<h3> "+descripcion+"</h3>\n"
#         for op in Operaciones:
#             html+="<p>"+op[1]+" =" + str(op[0])+ "</p>\n"

#         html+="""</body>
#         </html>"""

#         try:


#             with open("Resultados.html",'w') as file:
#                 file.write(html)

#                 file.close()
            
#         except:
#             print("No se pudo generar el html")

#         try:


#             with open("estiloDinamico.css",'w') as file:
#                 file.write(css)

#                 file.close()
            
#         except:
#             print("No se pudo generar el css")

#     def adivinarColor(self,color):
#         if color=="NEGRO":
#             return "black"
#         elif color=="ROJO":
#             return "red"
#         elif color=="NARANJA":
#             return "orange"
#         elif color=="AMARILLO":
#             return "yellow"
#         elif color=="AZUL":
#             return "blue"
#         elif color=="GRIS":
#             return "grey"
#         elif color=="CYAN":
#             return "cyan"
#         elif color=="CELESTE":
#             return "cyan"
#         elif color=="BLANCO":
#             return "white"
#         elif color=="MORADO":
#             return "purple"
#         elif color=="VERDE":
#             return "green"
#         else:
#             return "black"
        
        