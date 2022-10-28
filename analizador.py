
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
        i=0
        actual=""
        long = len(texto)
        while(i<long and texto[i]!=None):
            actual=texto[i]

            if estado==0:
                if actual.isalpha():
                    lexema+=actual
                    estado=7
                    i+=1
                    columna+=1
                    continue
                if actual.isdigit():
                    lexema+=actual
                    estado=15
                    i+=1
                    columna+=1
                    continue
                elif actual=="/":
                    lexema+= actual
                    tokens.append(token(tokentype.slash,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="=":
                    lexema+= actual
                    tokens.append(token(tokentype.igual,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual == '[':
                    lexema+= actual
                    tokens.append(token(tokentype.corcheteAbre,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== '<':
                    lexema+=actual
                    tokens.append(token(tokentype.menor,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='\"':
                    lexema+=actual
                    estado= 8
                    i+=1
                    columna+=1
                    continue
                elif actual=='>':
                    lexema+=actual
                    tokens.append(token(tokentype.mayor,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual==']':
                    lexema+=actual
                    tokens.append(token(tokentype.corcheteCierre,lexema,fila,columna))
                    lexema=""
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
                    errores.append(erroR(lexema,columna,fila))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
            elif estado==7:
                if actual.isalpha() or actual=="," or actual=="." or actual==":" or actual==";":
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    tokens.append(token(tokentype.letras,lexema,fila,columna-len(lexema)))
                    lexema=""
                    estado=0
                    continue
            elif estado == 8 :
                if actual=="\"":
                    estado=0
                    lexema+=actual
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
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
            elif estado ==15:
                if actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual==".":
                    estado=16
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    estado=0
                    tokens.append(token(tokentype.numero,lexema,fila,columna-len(lexema)))
                    lexema=""
                    continue
            elif estado ==16:
                if actual.isdigit():
                    estado=17
                    lexema+=actual
                    columna+=1
                    i+=1
                    continue
                else:
                    errores.append(erroR(lexema,columna-len(lexema),fila))
                    lexema=""
                    estado=0
                    continue
            elif estado==17:
                if actual.isdigit():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    estado=0
                    tokens.append(token(tokentype.decimal,lexema,fila,columna-len(lexema)))
                    lexema=""
                    continue




            
#        if estado==6 or estado == 12:
#            #print("Se esperaba un \" o un \' para finalizar la cadena")
#            errores+="Se esperaba un \" o un \' para finalizar la cadena"
        resultados = []
        resultados.append(tokens)
        resultados.append(errores)
        return resultados

    def cargarArchivo(self):
        Tk().withdraw()
        txt=""
        try:
            path = askopenfilename(filetypes=[('.lfp','*.lfp'),('*.*','*.*')])
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
                    <th>Tipo token</th>
                    <th>Lexema</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
            </thead>
<tbody>'''
        for obj in tokens:

            if obj.type == tokentype.letras:

                txt+= "<tr> <th> letras:1001</th>\n"
            
            elif obj.type == tokentype.corcheteAbre:

                txt+= "<tr> <th> corcheteAbre:1003</th>\n"
            elif obj.type == tokentype.menor:

                txt+= "<tr> <th> menor:1005</th>\n"
            
            elif obj.type == tokentype.cadena:

                txt+= "<tr> <th> cadena:1009</th>\n"
            
            elif obj.type == tokentype.mayor:

                txt+= "<tr> <th> mayor:1002</th>\n"
            elif obj.type == tokentype.corcheteCierre:

                txt+= "<tr> <th> corcheteCierre:1004</th>\n"
            elif obj.type == tokentype.igual:

                txt+= "<tr> <th> igual:1006</th>\n"
            elif obj.type == tokentype.numero:

                txt+= "<tr> <th> numero:1007</th>\n"
            elif obj.type == tokentype.slash:

                txt+= "<tr> <th> slash:1008</th>\n"  
            elif obj.type == tokentype.decimal:

                txt+= "<tr> <th> decimal:1010</th>\n"               

            
            txt+="<th> "+ str(obj.lexema)+ "</th>\n"
            txt+="<th> "+ str(obj.fila)+ "</th>\n"
            txt+="<th> "+ str(obj.columna)+ "</th>\n"
            
            txt+="</tr>"
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
                        <th>No.</th>
                        <th>Lexema</th>
                        <th>Tipo</th>
                        <th>Columna</th>
                        <th>Fila</th>
                        
                    </tr>
                </thead>
    <tbody>'''
        for obj in erroreslexicos:
            txt+="<tr> "
            txt+="<th> " + str(i)+ "</th>\n"
            txt+="<th> " + obj.lexema+ "</th>\n"
            txt+="<th> " + "Error" + "</th>\n"
            txt+="<th> " + str(obj.columna)+ "</th>\n"
            txt+="<th> " + str(obj.fila)+ "</th>\n"
                    
            #txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"
        
        txt+= '''
            </tbody>
        </table>
        <hr>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>
                        Errores Sintacticos
                    </th>
                </tr>
            </thead>
            <tbody>

            '''
        filas = erroresSintacticos.split('\n')
        for obj in filas:
                    
            txt+= "<tr> <th colspan=\"4\"> "+ obj + "</th>\n"
        
            txt+="</tr>"
        txt+= '''
            </tbody>
        </table>
        <hr>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>
                        Errores Semanticos
                    </th>
                </tr>
            </thead>
            <tbody>

            '''
        filas = erroresSemanticos.split('\n')
        for obj in filas:
                    
            txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"

        txt+='''
                </tbody>
            </table>
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
        
        