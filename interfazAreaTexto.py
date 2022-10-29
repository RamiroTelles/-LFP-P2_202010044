
from tkinter import *

from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
#from typing import TextIO
from tkinter import ttk
#from click import style
from analizador import analizador
from os import startfile
from sintact import analSitac
from generadorForm import generadorForm

#from matplotlib.pyplot import text

class interfazAreaTexto():

    
    def __init__(self) -> None:
        self.funciones = analizador()
        self.generador= generadorForm()
      
        
        def cargarArchivo():
            opcion = cajaCombo2.get()

            
            if opcion=="Abrir":
                texto=self.funciones.cargarArchivo()
                t_editor.delete("1.0","end")
                t_editor.insert("1.0",texto)
            elif opcion=="Guardar":
                texto= t_editor.get("1.0","end")
                self.funciones.guardar(texto)
            elif opcion=="Guardar Como":
                texto= t_editor.get("1.0","end")
                self.funciones.guardarComo()
                self.funciones.guardar(texto)
                pass
            elif opcion=="Salir":
                ventana.destroy()
                exit()

            
            pass
        
        def analizar():
            texto =t_editor.get("1.0","end")
            #print(texto)
            result1= self.funciones.analizadorLexico(texto)
            
            self.funciones.reporteTokens(result1[0])
            asm= analSitac(result1[0])
            self.funciones.reporteErrores(result1[1],asm.errores,"")
            self.generador.crearCSS(asm.etiquetas,asm.botones,asm.checks,asm.radiobotones,asm.cTextos,asm.cAreaTextos,asm.cClaves,asm.contenedores)
            self.generador.crearHTML(asm.etiquetas,asm.botones,asm.checks,asm.radiobotones,asm.cTextos,asm.cAreaTextos,asm.cClaves,asm.contenedores)
            pass
        
        def mostrarErrores():
            startfile("ReporteErrores.html")
            pass

        def mostrarTokens():
            startfile("ReporteTokens.html")
        # def generarReporte():

        #     opcion = cajaCombo.get()

            
        #     if opcion=="Manual de Usuario":
        #         startfile("ManualDeUsuario.pdf")
        #     elif opcion=="Manual Técnico":
        #         startfile("ManualTecnico.pdf")
        #     elif opcion=="Temas de Ayuda":
        #         messagebox.showinfo(message="Creado Por Ramiro Agustín Télles Carcuz \n Carnet: 202010044",title="Temas de Ayuda")
        #     pass

        ventana = Tk()

        ventana.geometry("800x600")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)

        

        b_Analizar = Button(ventana,text="Generar Página web", command=analizar)
        b_Cargar = Button(ventana, text="Menú", command=cargarArchivo)
        b_errores= Button(ventana, text="Área de Errores", command=mostrarErrores)
        b_tokens = Button(ventana, text="Menú Tokens", command=mostrarTokens)
         

        b_Cargar.place(x=30,y=45)
        b_errores.place(x=390,y=45)
        b_tokens.place(x=550,y=45)
        b_Analizar.place(x=230,y=45)

        t_editor = ScrolledText(ventana,width=91,height=28)
        #ScrolVer = Scrollbar(ventana, command=t_editor.yview)
        #cajaCombo = ttk.Combobox(ventana,values=["Manual de Usuario","Manual Técnico","Temas de Ayuda"],state="readonly")
        cajaCombo2 = ttk.Combobox(ventana,values=["Abrir","Guardar","Guardar Como","Salir"],state="readonly")
        
        t_editor.place(x=30,y=80)
        #cajaCombo.place(x=280,y=45)
        cajaCombo2.place(x=80,y=45)
        cajaCombo2.current(0)
        #cajaCombo.current(0)

        #ScrolVer.place(x=760,y=80)
        

        ventana.mainloop()
        pass