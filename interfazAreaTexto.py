
from tkinter import *

from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from typing import TextIO
from tkinter import ttk
#from click import style
from analizador import analizador
from os import startfile
from sintact import analSitac

#from matplotlib.pyplot import text

class interfazAreaTexto():

    
    def __init__(self) -> None:
        self.funciones = analizador()
      
        
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
            elif opcion=="Analizar":
                texto =t_editor.get("1.0","end")
                #print(texto)
                result1= self.funciones.analizadorLexico(texto)
            
                self.funciones.reporteTokens(result1[0])
                asm= analSitac(result1[0])
                self.funciones.reporteErrores(result1[1],asm.errores,"")
                self.funciones.generarResultados(asm.title,asm.titleColor,asm.titleTam,asm.txt,asm.descColor,asm.descTam,asm.Operaciones,asm.conColor,asm.conTam)
                startfile("Resultados.html")

            elif opcion=="Errores":
                startfile("ReporteErrores.html")
            elif opcion=="Salir":
                ventana.destroy()
                exit()

            
            pass
        
        def analizar():
            texto =t_editor.get("1.0","end")
            print(texto)
            result1= self.funciones.analizadorLexico(texto)
            
            self.funciones.reporteTokens(result1[0])
            asm= analSitac(result1[0])
            self.funciones.reporteErrores(result1[1],asm.errores,"")

            # result3 = self.funciones.analSemantico(result2[0],texto)
     

            # self.funciones.reporteTokens(result1[0])
            # self.funciones.reporteErrores(result1[1],result2[1],result3[2])
            # startfile("dynamicForm.html")
            pass

        def generarReporte():

            opcion = cajaCombo.get()

            
            if opcion=="Manual de Usuario":
                startfile("ManualDeUsuario.pdf")
            elif opcion=="Manual Técnico":
                startfile("ManualTecnico.pdf")
            elif opcion=="Temas de Ayuda":
                messagebox.showinfo(message="Creado Por Ramiro Agustín Télles Carcuz \n Carnet: 202010044",title="Temas de Ayuda")
            pass
        ventana = Tk()

        ventana.geometry("800x600")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)

        #b_volver = Button(ventana,text="volver")

        #b_analizar = Button(ventana,text="Analizar", command=analizar)

        b_reporte = Button(ventana,text="Ayuda", command=generarReporte)
        b_Cargar = Button(ventana, text="Menú", command=cargarArchivo)
         

        b_Cargar.place(x=30,y=45)

        #b_analizar.place(x=50,y=540)

        b_reporte.place(x=230,y=45)

        t_editor = ScrolledText(ventana,width=91,height=28)
        #ScrolVer = Scrollbar(ventana, command=t_editor.yview)
        cajaCombo = ttk.Combobox(ventana,values=["Manual de Usuario","Manual Técnico","Temas de Ayuda"],state="readonly")
        cajaCombo2 = ttk.Combobox(ventana,values=["Abrir","Guardar","Guardar Como","Analizar","Errores","Salir"],state="readonly")
        
        t_editor.place(x=30,y=80)
        cajaCombo.place(x=280,y=45)
        cajaCombo2.place(x=80,y=45)
        cajaCombo2.current(0)
        cajaCombo.current(0)

        #ScrolVer.place(x=760,y=80)
        

        ventana.mainloop()
        pass