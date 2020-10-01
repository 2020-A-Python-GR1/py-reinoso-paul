#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:56:20 2020

@author: Reinoso Paul - Revelo Karla
"""

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
import sys
from tkinter import filedialog as fd
from PIL import ImageFont, Image, ImageChops, ImageEnhance, ImageOps, ImageColor, ImageDraw

class Aplicacion():
    def __init__(self):
        global inicio
        inicio = tk.Tk()        
        inicio.title('')
        inicio.update_idletasks()
        width = inicio.winfo_width()  
        width = width + 200
        height = inicio.winfo_height()   
        height = height + 310
        x = (inicio.winfo_screenwidth() // 2) - (width // 2)
        y = (inicio.winfo_screenheight() // 2) - (height // 2)
        inicio.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        #self.inicio.geometry('400x510') # anchura x altura
        image2 = Image.open("fondo.png")        
        image2 = image2.resize((420, 420), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image2)                
        background_label = Label(inicio, image=image1)
        background_label.image=image1
        background_label.place(x=0, y=0, height=420, width=420)        

        fontStyle = tkFont.Font(family="Arial", size=12)

        botonCargar = tk.Button(inicio, text='CARGAR IMAGEN', font=fontStyle, bg = '#22201C', fg = 'white',
                 height = 5, width=60, command = apt_imagen).pack(side=BOTTOM)

        inicio.mainloop()
def main():
    mi_app = Aplicacion()
    return 0

def apt_imagen():
    nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))    
    if nombrearch!='':                 
        imagenC = Image.open(nombrearch)                
        imagenC = imagenC.resize((400, 410), Image.ANTIALIAS)        
        guardar_imagen(imagenC)                      

def guardar_imagen(imag):               
        global pantallaPrincipal          
        pantallaPrincipal = tk.Toplevel()
        pantallaPrincipal.geometry('400x510') 
        pantallaPrincipal.title('')
        pantallaPrincipal.update_idletasks()
        width = pantallaPrincipal.winfo_width()          
        height = pantallaPrincipal.winfo_height()           
        x = (pantallaPrincipal.winfo_screenwidth() // 2) - (width // 2)
        y = (pantallaPrincipal.winfo_screenheight() // 2) - (height // 2)
        pantallaPrincipal.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        pantallaPrincipal.configure(bg = 'white') 
        image2 = ImageTk.PhotoImage(imag)        
        background_label = Label(pantallaPrincipal, image=image2)
        background_label.image=image2
        background_label.place(x=0, y=60, height=385, width=400)                
        fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')
        botonInicio = tk.Button(pantallaPrincipal, text='INICIO', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, 
                  command = pantallaPrincipal.destroy).place(x=0, y=0)               
        botonGuardar = tk.Button(pantallaPrincipal, text='GUARDAR', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, command= lambda: guardar_imagenjpg(imag)).place(x=310, y=0)    
        botonDimensiones = tk.Button(pantallaPrincipal, text='DIMENSIONES', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=12, 
                  command = lambda: dimensiones(imag)).place(x=0, y=460)       
        botonTexto = tk.Button(pantallaPrincipal, text='TEXTO', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=8, 
                  command = lambda: cuadro_texto(imag)).place(x=110, y=460)
        botonEfectos = tk.Button(pantallaPrincipal, text='EFECTOS', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=10, 
                  command = lambda: efectos(imag)).place(x=187, y=460)      
        botonSuperpo = tk.Button(pantallaPrincipal, text='SUPERPOSICION', font=fontStyle, bg = 'white', fg = 'black',
                  height = 2, width=14, 
                  command = lambda: superposicion(imag)).place(x=280, y=460)                        

def guardar_imagenjpg(imag):
    imag.save("imagen_editada.png")
    inicio.destroy()
    main()
    
def dimensiones(imag):                
        pantallaDimensiones = tk.Toplevel()        
        pantallaDimensiones.title('')
        pantallaDimensiones.update_idletasks()
        width = pantallaDimensiones.winfo_width()        
        width = width + 200
        height = pantallaDimensiones.winfo_height()   
        height = height + 310
        x = (pantallaDimensiones.winfo_screenwidth() // 2) - (width // 2)
        y = (pantallaDimensiones.winfo_screenheight() // 2) - (height // 2)
        pantallaDimensiones.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        pantallaDimensiones.configure(bg = 'white')  
        image2 = ImageTk.PhotoImage(imag)        
        background_label = Label(pantallaDimensiones, image=image2)
        background_label.image=image2
        background_label.place(x=0, y=60, height=385, width=400)                
        fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')
        botonAtras = tk.Button(pantallaDimensiones, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=10, 
             command= pantallaDimensiones.destroy).place(x=0, y=0)    
        botonCortar = tk.Button(pantallaDimensiones, text='CORTAR', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25, 
             command = lambda: cortar(imag)).place(x=0, y=460)
        botonRotar = tk.Button(pantallaDimensiones, text='ROTAR', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25, 
             command = lambda: rotar(imag)).place(x=200, y=460)    
        pantallaDimensiones.mainloop()        
            
def cortar(imag):      
    global pantallaCorte 
    global corte
    global box
    pantallaCorte = tk.Toplevel()    
    pantallaCorte.title('')
    pantallaCorte.update_idletasks()
    width = pantallaCorte.winfo_width()  
    width = width + 200
    height = pantallaCorte.winfo_height()   
    height = height + 310
    x = (pantallaCorte.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaCorte.winfo_screenheight() // 2) - (height // 2)
    pantallaCorte.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaCorte.configure(bg = 'white')    
    image2 = ImageTk.PhotoImage(imag)        
    background_label = Label(pantallaCorte, image=image2)
    background_label.image=image2
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')         
    botonAtras = tk.Button(pantallaCorte, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = pantallaCorte.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaCorte, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)        
    corteCuadrado = tk.Button(pantallaCorte, text='CUADRADO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: corte_cuadrado(imag)).place(x=0, y=460)    
    corte_1 = tk.Button(pantallaCorte, text='4:3', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: corte1(imag)).place(x=100, y=460)
    corte_2 = tk.Button(pantallaCorte, text='3:2', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: corte2(imag)).place(x=200, y=460)
    corte_3 = tk.Button(pantallaCorte, text='16:9', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, 
              command = lambda: corte3(imag)).place(x=300, y=460)            
    pantallaCorte.bind("<Button-1>", lambda evento: callback(evento, imag))    
    pantallaCorte.bind("<Button-3>", callback2)    

def callback(event, imag):    
    global evento
    global corte
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[2] == "button3"):
        print("corte_cuadrado")
        corte = "corte_cuadrado()"
        imgCorte = corte_cuadrado(imag)
        print(corte)
    elif(evento_string[2] == "button4"):
        print("corte1") 
        corte = "corte1()"
        imgCorte = corte1(imag)
        print(corte)
    elif(evento_string[2] == "button5"):
        print("corte2")
        corte = "corte2()"
        imgCorte = corte2(imag)
        print(corte)
    elif(evento_string[2] == "button6"):
        print("corte3")
        corte = "corte3()"
        imgCorte = corte3(imag)
        print(corte)
    #print(type(evento_string))
    #comparaciones(evento_string)    
def callback2(event):
    print("entro al 2")
    print(corte)
    if(corte == "corte_cuadrado()"):
        guardar_imagen(imgCorte)
    elif(corte == "corte1()"):
        guardar_imagen(imgCorte)
    if(corte == "corte2()"):
        guardar_imagen(imgCorte)
    if(corte == "corte3()"):
        guardar_imagen(imgCorte)
        
def corte_cuadrado(imag):    
    box = (100, 100, 400, 400)       
    area_recortada = imag.crop(box)         
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)
    return area_recortada                    

def corte1(imag):    
    box = (50, 50, 400, 400)    
    area_recortada = imag.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)       
    return area_recortada                 
    
def corte2(imag):    
    box = (200, 200, 400, 400)
    area_recortada = imag.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return area_recortada                  

def corte3(imag):    
    box = (160, 160, 500, 500)
    area_recortada = imag.crop(box)
    #img = ImageTk.PhotoImage(area_recortada)
    image1 = ImageTk.PhotoImage(area_recortada)
    background_label = Label(pantallaCorte, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return area_recortada
            
def rotar(imag):    
    global pantallaRotar    
    pantallaRotar = tk.Toplevel()    
    pantallaRotar.title('')
    pantallaRotar.update_idletasks()
    width = pantallaRotar.winfo_width()  
    width = width + 200
    height = pantallaRotar.winfo_height()   
    height = height + 310
    x = (pantallaRotar.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaRotar.winfo_screenheight() // 2) - (height // 2)
    pantallaRotar.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaRotar.configure(bg = 'white')
    image2 = ImageTk.PhotoImage(imag)        
    background_label = Label(pantallaRotar, image=image2)
    background_label.image=image2
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaRotar, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaRotar.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaRotar, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    rIzquierda = tk.Button(pantallaRotar, text='IZQUIERDA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: izquierda(imag)).place(x=0, y=460)
    rDerecha = tk.Button(pantallaRotar, text='DERECHA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: derecha(imag)).place(x=100, y=460)
    rHorizontal = tk.Button(pantallaRotar, text='HORIZONTAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = lambda: horizontal(imag)).place(x=200, y=460)
    rVertical = tk.Button(pantallaRotar, text='VERTICAL', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, 
              command = lambda: vertical(imag)).place(x=300, y=460)
    pantallaRotar.bind("<Button-1>", lambda evento: callback3(evento, imag))    
    pantallaRotar.bind("<Button-3>", callback4)    

def callback3(event, imag):
    global evento
    global rotacion
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[2] == "button3"):
        print("izquierda")
        rotacion = "izquierda()"
        imgCorte = izquierda(imag)
        print(corte)
    elif(evento_string[2] == "button4"):
        print("derecha") 
        rotacion = "derecha()"
        imgCorte = derecha(imag)
        print(corte)
    elif(evento_string[2] == "button5"):
        print("horizontal")
        rotacion = "horizontal()"
        imgCorte = horizontal(imag)
        print(corte)
    elif(evento_string[2] == "button6"):
        print("vertical")
        rotacion = "vertical()"
        imgCorte = vertical(imag)
        print(corte)
    

def callback4(event):
    print("entro al 4")
    print(rotacion)
    if(rotacion == "izquierda()"):
        guardar_imagen(imgCorte)
    elif(rotacion == "derecha()"):
        guardar_imagen(imgCorte)
    if(rotacion == "horizontal()"):
        guardar_imagen(imgCorte)
    if(rotacion == "vertical()"):
        guardar_imagen(imgCorte)

def izquierda(imag):    
    img_rotada = imag.transpose(Image.ROTATE_90)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return img_rotada                      

def derecha(imag):    
    img_rotada = imag.transpose(Image.ROTATE_270)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return img_rotada  
    
def horizontal(imag): 
    img_rotada = ImageOps.mirror(imag)    
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return img_rotada  
    
def vertical(imag):
    img_horizontal = ImageOps.mirror(imag)    
    img_rotada = img_horizontal.transpose(Image.ROTATE_180)
    image1 = ImageTk.PhotoImage(img_rotada)
    background_label = Label(pantallaRotar, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return img_rotada  

def efectos(imag): 
    global pantallaEfectos 
    global canvas1    
    pantallaEfectos = tk.Toplevel()    
    pantallaEfectos.title('')
    pantallaEfectos.update_idletasks()
    width = pantallaEfectos.winfo_width()  
    width = width + 200
    height = pantallaEfectos.winfo_height()   
    height = height + 310
    x = (pantallaEfectos.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaEfectos.winfo_screenheight() // 2) - (height // 2)
    pantallaEfectos.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaEfectos.configure(bg = 'white')    
    image2= ImageTk.PhotoImage(imag)
    background_label = Label(pantallaEfectos, image=image2)
    background_label.image=image2
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')                 
    botonAtras = tk.Button(pantallaEfectos, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, command = pantallaEfectos.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaEfectos, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    frame1=tk.Frame(pantallaEfectos,bg='white')
    frame1.place(x=0,y=440)
    canvas1=tk.Canvas(frame1)
    frame2=tk.Frame(canvas1,bg='white',relief='groove',bd=1,width=1230,height=430)
    scrollbar1=tk.Scrollbar(frame1,orient="horizontal",command=canvas1.xview)
    canvas1.configure(xscrollcommand=scrollbar1.set)
    scrollbar1.pack(side=BOTTOM,fill=X)
    canvas1.pack(side=BOTTOM)
    canvas1.create_window((0,0),window=frame2,anchor='nw')
    frame2.bind("<Configure>",ScrollAll)
    
    bLuz = tk.Button(frame2, text='LUZ', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = lambda: luz(imag)).place(x=0, y=10)        
    bContraste = tk.Button(frame2, text='CONTRASTE', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = lambda: contraste(imag)).place(x=100, y=10)
    bSaturacion = tk.Button(frame2, text='SATURACION', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14, command = lambda: saturacion(imag)).place(x=202, y=10)
    bTemperatura = tk.Button(frame2, text='TEMPERATURA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14, command = lambda: temperatura(imag)).place(x=325, y=10)
    bIC = tk.Button(frame2, text='I/C', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = lambda: ic(imag)).place(x=445, y=10)    
    bBN = tk.Button(frame2, text='B/N', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11, command = lambda: bn(imag)).place(x=545, y=10)    
    pantallaEfectos.bind("<Button-1>", lambda evento: callback5(evento, imag))    
    pantallaEfectos.bind("<Button-3>", callback6)
    
def callback5(event, imag):
    global evento
    global efecto
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[5] == "button"):
        print("luz")
        efecto = "luz()"
        imgCorte = luz(imag)
        print(efecto)
    elif(evento_string[5] == "button2"):
        print("contraste") 
        efecto = "contraste()"
        imgCorte = contraste(imag)
        print(efecto)
    elif(evento_string[5] == "button3"):
        print("saturacion")
        efecto = "saturacion()"
        imgCorte = saturacion(imag)
        print(efecto)
    elif(evento_string[5] == "button4"):
        print("temperatura")
        efecto = "temperatura()"
        imgCorte = temperatura(imag)
        print(efecto)
    elif(evento_string[5] == "button5"):
        print("ic")
        efecto = "ic()"
        imgCorte = ic(imag)
        print(efecto)
    elif(evento_string[5] == "button6"):
        print("bn")
        efecto = "bn()"
        imgCorte = bn(imag)
        print(efecto)
    

def callback6(event):
    print("entro al 6")
    print(efecto)
    if(efecto == "luz()"):
        guardar_imagen(imgCorte)
    elif(efecto == "contraste()"):
        guardar_imagen(imgCorte)
    elif(efecto == "saturacion()"):
        guardar_imagen(imgCorte)
    elif(efecto == "temperatura()"):
        guardar_imagen(imgCorte)
    elif(efecto == "ic()"):
        guardar_imagen(imgCorte)
    elif(efecto == "bn()"):
        guardar_imagen(imgCorte)

def ScrollAll(event):
    canvas1.configure(scrollregion=(0,0,650,650),width=400,height=60,bg='white')

def luz(imag):    
    imagen_efecto = ImageEnhance.Brightness(imag).enhance(2)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)       
    return imagen_efecto                 
    
def contraste(imag):    
    imagen_efecto = ImageEnhance.Contrast(imag).enhance(4)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)  
    return imagen_efecto                  

def saturacion(imag):    
    imagen_efecto = ImageOps.equalize(imag)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return imagen_efecto

def temperatura(imag):
    imagen_gris = ImageOps.grayscale(imag)
    imagen_efecto = ImageOps.colorize(imagen_gris, "black", "yellow")
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return imagen_efecto

def ic(imag):    
    imagen_efecto = ImageChops.invert(imag)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return imagen_efecto

def bn(imag):    
    imagen_efecto = ImageOps.grayscale(imag)
    image1 = ImageTk.PhotoImage(imagen_efecto)
    background_label = Label(pantallaEfectos, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    return imagen_efecto
        
def superposicion(imag):    
    global pantallaSuperpo    
    pantallaSuperpo = tk.Toplevel()    
    pantallaSuperpo.title('')
    pantallaSuperpo.update_idletasks()
    width = pantallaSuperpo.winfo_width()  
    width = width + 200
    height = pantallaSuperpo.winfo_height()   
    height = height + 310
    x = (pantallaSuperpo.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaSuperpo.winfo_screenheight() // 2) - (height // 2)
    pantallaSuperpo.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaSuperpo.configure(bg = 'white')    
    image2 = ImageTk.PhotoImage(imag)
    background_label = Label(pantallaSuperpo, image=image2)
    background_label.image=image2
    background_label.place(x=0, y=60, height=385, width=400)                
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaSuperpo, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = pantallaSuperpo.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaSuperpo, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
   
    img = Image.open('icono_cuadrado.png')    
    img = img.resize((56, 56), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoCuadrado = ImageTk.PhotoImage(img)
    bCuadrado = Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoCuadrado, 
              compound="right", command = lambda: s_cuadrado(imag))    
    bCuadrado.image = iconoCuadrado
    bCuadrado.place(x=0, y=460)
    
    img1 = Image.open('icono_ovalo.png')    
    img1 = img1.resize((30, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoOvalo = ImageTk.PhotoImage(img1)
    bOvalo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoOvalo, 
              compound="right", command = lambda: s_ovalo(imag))
    bOvalo.image = iconoOvalo
    bOvalo.place(x=68, y=460)
    
    img2 = Image.open('icono_triangulo.png')    
    img2 = img2.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoTriangulo = ImageTk.PhotoImage(img2)
    bTriangulo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoTriangulo,
              compound="right", command = lambda: s_triangulo(imag))
    bTriangulo.image = iconoTriangulo
    bTriangulo.place(x=136, y=460)
    
    img3 = Image.open('icono_triangulo2.jpg')    
    img3 = img3.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoTriangulo2 = ImageTk.PhotoImage(img3)
    btInvertido = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60,  image=iconoTriangulo2, 
              compound="right", command = lambda: s_trianguloIn(imag))
    btInvertido.image = iconoTriangulo2
    btInvertido.place(x=204, y=460)
    
    img4 = Image.open('icono_circulo.png')    
    img4 = img4.resize((40, 40), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoCirculo = ImageTk.PhotoImage(img4)
    bCirculo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoCirculo, 
              compound="right", command = lambda: s_circulo(imag))
    bCirculo.image = iconoCirculo
    bCirculo.place(x=270, y=460)    
    
    img5 = Image.open('icono_rectangulo.jpg')    
    img5 = img5.resize((40, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    iconoRectangulo = ImageTk.PhotoImage(img5)
    bRectangulo = tk.Button(pantallaSuperpo, font=fontStyle, bg = 'white', fg = 'black',
              height = 50, width=60, image=iconoRectangulo, 
              compound="right", command = lambda: s_rectangulo(imag))
    bRectangulo.image = iconoRectangulo
    bRectangulo.place(x=336, y=460)    
    
    pantallaSuperpo.bind("<Button-1>", lambda evento: callback7(evento, imag))    
    pantallaSuperpo.bind("<Button-3>", callback8)    

def callback7(event, imag):
    global evento
    global superp
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[2] == "button3"):
        print("s_cuadrado")
        superp = "s_cuadrado()"
        imgCorte = s_cuadrado(imag)
        print(superp)
    elif(evento_string[2] == "button4"):
        print("s_ovalo") 
        superp = "s_ovalo()"
        imgCorte = s_ovalo(imag)
        print(superp)
    elif(evento_string[2] == "button5"):
        print("s_triangulo")
        superp = "s_triangulo()"
        imgCorte = s_triangulo(imag)
        print(superp)
    elif(evento_string[2] == "button6"):
        print("s_trianguloIn")
        superp = "s_trianguloIn()"
        imgCorte = s_trianguloIn(imag)
        print(superp)
    elif(evento_string[2] == "button7"):
        print("s_circulo")
        superp = "s_circulo()"
        imgCorte = s_circulo(imag)
        print(superp)
    elif(evento_string[2] == "button8"):
        print("s_rectangulo")
        superp = "s_rectangulo()"
        imgCorte = s_rectangulo(imag)
        print(superp)
    
def callback8(event):
    print("entro al 8")
    print(superp)
    if(superp == "s_cuadrado()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_ovalo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_triangulo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_trianguloIn()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_circulo()"):
        guardar_imagen(imgCorte)
    elif(superp == "s_rectangulo()"):
        guardar_imagen(imgCorte)

def s_cuadrado(imag):
    img = Image.open("cuadrado.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)    
    return img 

def s_ovalo(imag):
    img = Image.open("ovalo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)         
    return img 

def s_triangulo(imag):
    img = Image.open("triangulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)         
    return img 

def s_trianguloIn(imag):
    img = Image.open("trianguloInvertido.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)    
    return img 

def s_circulo(imag):
    img = Image.open("circulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)        
    return img     

def s_rectangulo(imag):
    img = Image.open("rectangulo.jpeg")            
    img = img.resize((400, 410), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(img)
    background_label = Label(pantallaSuperpo, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)           
    return img 

def cuadro_texto(imag):
    global pantallaTexto 
    global entry
    pantallaTexto = tk.Toplevel()    
    pantallaTexto.title('')
    pantallaTexto.update_idletasks()
    width = pantallaTexto.winfo_width()  
    width = width + 200
    height = pantallaTexto.winfo_height()       
    x = (pantallaTexto.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaTexto.winfo_screenheight() // 2) - (height // 2)
    pantallaTexto.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaTexto.configure(bg = 'white')
    pantallaTexto.state(newstate = "normal")
    entry = ttk.Entry(pantallaTexto)
    entry.place(x=20, y=50, height=80, width=360)          
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaTexto, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 1, width=10, command = pantallaTexto.destroy).place(x=0, y=0)
    botonListo = tk.Button(pantallaTexto, text='LISTO', font=fontStyle, bg = 'black', fg = 'white',
              height = 2, width=80, 
              command= lambda: texto_imagen(entry, imag)).pack(side=BOTTOM)    
    
def texto_imagen(entry, imag):    
    global pantallaImgTx
    global entrada
    pantallaImgTx = tk.Toplevel()    
    pantallaImgTx.title('')
    pantallaImgTx.update_idletasks()
    width = pantallaImgTx.winfo_width()  
    width = width + 200
    height = pantallaImgTx.winfo_height()   
    height = height + 310
    x = (pantallaImgTx.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaImgTx.winfo_screenheight() // 2) - (height // 2)
    pantallaImgTx.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaImgTx.configure(bg = 'white')        
    entrada = entry.get()
    print("soy la entrada:" +entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(255,255,255,255))    
    final = Image.alpha_composite(imag, texto)    
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaImgTx, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = pantallaImgTx.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaImgTx, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    bColor = tk.Button(pantallaImgTx, text='COLOR', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25, 
             command = lambda: cuadro_color(entrada, imag)).place(x=0, y=460)
    bAlineacion = tk.Button(pantallaImgTx, text='ALINEACION', font=fontStyle, bg = 'white', fg = 'black',
             height = 2, width=25).place(x=200, y=460)                     
    pantallaImgTx.bind("<Button-1>", lambda evento: callback13(evento, imag))    
    pantallaImgTx.bind("<Button-3>", callback10)    
    #pantallaImgTx.mainloop()

def cuadro_color(entrada, imag):
    global pantallaColor     
    pantallaColor = tk.Toplevel()    
    pantallaColor.title('')
    pantallaColor.update_idletasks()
    width = pantallaColor.winfo_width()  
    width = width + 200
    height = pantallaColor.winfo_height()   
    x = (pantallaColor.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaColor.winfo_screenheight() // 2) - (height // 2)
    pantallaColor.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaColor.configure(bg = 'white')        
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaColor, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 1, width=10, 
              command = pantallaColor.destroy).place(x=0, y=0)
    bBlanco = tk.Button(pantallaColor, bg = 'white',
              height = 2, width=3,
              command = lambda: texto_blanco(pantallaColor, entrada, imag)).place(x=60, y=80)
    bNegro = tk.Button(pantallaColor, bg = 'black',
              height = 2, width=3, 
              command = lambda: texto_negro(pantallaColor, entrada, imag)).place(x=115, y=80)
    bRojo = tk.Button(pantallaColor, bg = 'red',
              height = 2, width=3,
              command = lambda: texto_rojo(pantallaColor, entrada, imag)).place(x=170, y=80)
    bVerde = tk.Button(pantallaColor, bg = 'green',
              height = 2, width=3,
              command = lambda: texto_verde(pantallaColor, entrada, imag)).place(x=225, y=80)
    bAzul = tk.Button(pantallaColor, bg = 'blue',
              height = 2, width=3,
              command = lambda: texto_azul(pantallaColor, entrada, imag)).place(x=280, y=80)    
    pantallaColor.bind("<Button-1>", lambda evento: callback9(evento, imag))        

def callback9(event, imag):
    global evento
    global color
    global colorT
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[2] == "button2"):
        print("texto_blanco")
        color = "texto_blanco()"
        colorT = (255,255,255,255)
        imgCorte = texto_blanco(pantallaColor, entrada, imag)
        print(color)
        print(colorT)
    elif(evento_string[2] == "button3"):
        print("texto_negro")         
        color = "texto_negro()"
        colorT = (0,0,0)
        imgCorte = texto_negro(pantallaColor, entrada, imag)        
        print(color)
        print(colorT)
    elif(evento_string[2] == "button4"):
        print("texto_rojo") 
        color = "texto_rojo()"
        colorT = (255,0,0)
        imgCorte = texto_rojo(pantallaColor, entrada, imag)
        print(color)
        print(colorT)
    elif(evento_string[2] == "button5"):
        print("texto_verde") 
        color = "texto_verde()"
        colorT = (0,255,0)
        imgCorte = texto_verde(pantallaColor, entrada, imag)
        print(color)
        print(colorT)        
    elif(evento_string[2] == "button6"):
        print("texto_azul") 
        color = "texto_azul()"
        colorT = (0,0,255)
        imgCorte = texto_azul(pantallaColor, entrada, imag)
        print(color)
        print(colorT)
        
def callback13(event, imag):
    print("entro al 13")
    global evento
    global color    
    global imgCorte    
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    if(evento_string[2] == "button4"):
        print("alineacion") 
        color = "alineacion()"        
        alineacion(entrada,imag,colorT)
        print(color)    

def callback10(event):
    print("entro al 10")
    print(color)
    if(color == "texto_blanco()"):
        guardar_imagen(imgCorte)
    elif(color == "texto_negro()"):
        guardar_imagen(imgCorte)
    elif(color == "texto_rojo()"):
        guardar_imagen(imgCorte)
    elif(color == "texto_verde()"):
        guardar_imagen(imgCorte)
    elif(color == "texto_azul()"):
        guardar_imagen(imgCorte)
        
def texto_negro(pantallaColor,entrada, imag):    
    print(entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(0,0,0))    
    final = Image.alpha_composite(imag, texto)      
    pantallaColor.destroy()
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)     
    return final    

def texto_blanco(pantallaColor,entrada, imag):    
    print(entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(255,255,255,255))    
    final = Image.alpha_composite(imag, texto)      
    pantallaColor.destroy()
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final  
                
def texto_rojo(pantallaColor,entrada, imag):
    print(entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(255,0,0))    
    final = Image.alpha_composite(imag, texto)      
    pantallaColor.destroy()
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final 

def texto_verde(pantallaColor,entrada, imag):    
    print(entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(0,255,0))    
    final = Image.alpha_composite(imag, texto)      
    pantallaColor.destroy()
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final                  

def texto_azul(pantallaColor,entrada,imag):    
    print(entrada)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=(0,0,255))    
    final = Image.alpha_composite(imag, texto)      
    pantallaColor.destroy()
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaImgTx, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final  
                
def alineacion(entrada, imag, colorT):    
    global pantallaAlineacion
    global canvas2 
    print(colorT)    
    pantallaAlineacion = tk.Toplevel()    
    pantallaAlineacion.title('')
    pantallaAlineacion.update_idletasks()
    width = pantallaAlineacion.winfo_width()  
    width = width + 200
    height = pantallaAlineacion.winfo_height()   
    height = height + 310
    x = (pantallaAlineacion.winfo_screenwidth() // 2) - (width // 2)
    y = (pantallaAlineacion.winfo_screenheight() // 2) - (height // 2)
    pantallaAlineacion.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pantallaAlineacion.configure(bg = 'white')
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)    
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400)                    
    fontStyle = tkFont.Font(family="Arial", size=10, weight = 'bold')             
    botonAtras = tk.Button(pantallaAlineacion, text='ATRAS', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10, 
              command = pantallaAlineacion.destroy).place(x=0, y=0)
    botonAceptar = tk.Button(pantallaAlineacion, text='ACEPTAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=10).place(x=310, y=0)
    
    frame2=tk.Frame(pantallaAlineacion,bg='white')
    frame2.place(x=0,y=440)
    canvas2=tk.Canvas(frame2)
    frame3=tk.Frame(canvas2,bg='white',relief='groove',bd=1,width=1230,height=430)
    scrollbar2=tk.Scrollbar(frame2,orient="horizontal",command=canvas2.xview)
    canvas2.configure(xscrollcommand=scrollbar2.set)
    scrollbar2.pack(side=BOTTOM,fill=X)
    canvas2.pack(side=BOTTOM)
    canvas2.create_window((0,0),window=frame3,anchor='nw')
    frame3.bind("<Configure>",ScrollAll1)
    
    bCentrar = tk.Button(frame3, text='CENTRAR', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11,
              command = lambda: centrar(entrada, imag, colorT)).place(x=0, y=10)        
    bArriba = tk.Button(frame3, text='ARRIBA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11,
              command = lambda: arriba(entrada, imag, colorT)).place(x=100, y=10)
    bAbajo = tk.Button(frame3, text='ABAJO', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14,
              command = lambda: abajo(entrada, imag, colorT)).place(x=202, y=10)
    bIzquierda = tk.Button(frame3, text='IZQUIERDA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=14,
              command = lambda: texto_izquierda(entrada, imag, colorT)).place(x=325, y=10)
    bDerecha = tk.Button(frame3, text='DERECHA', font=fontStyle, bg = 'white', fg = 'black',
              height = 2, width=11,
              command = lambda: texto_derecha(entrada, imag,colorT)).place(x=445, y=10)        
    pantallaAlineacion.bind("<Button-1>", lambda evento: callback11(evento, imag, colorT))    
    pantallaAlineacion.bind("<Button-3>", callback12)    

def ScrollAll1(event):
    canvas2.configure(scrollregion=(0,0,600,600),width=400,height=60,bg='white')

def callback11(event, imag, colorT):
    global evento
    global alin
    global imgCorte
    evento = event.widget 
    evento_str = str(evento)
    evento_string = evento_str.split('!')
    print(evento_string)
    if(evento_string[5] == "button"):
        print("centrar")
        alin = "centrar()"
        imgCorte = centrar(entrada, imag, colorT)
        print(alin)
    elif(evento_string[5] == "button2"):
        print("arriba")
        alin = "arriba()"
        imgCorte = arriba(entrada, imag, colorT)
        print(alin)
    elif(evento_string[5] == "button3"):
        print("abajo")
        alin = "abajo()"
        imgCorte = abajo(entrada, imag, colorT)
        print(alin)
    elif(evento_string[5] == "button4"):
        print("izquierda")
        alin = "texto_izquierda()"
        imgCorte = texto_izquierda(entrada, imag, colorT)
        print(alin)
    elif(evento_string[5] == "button5"):
        print("derecha")
        alin = "texto_derecha()"
        imgCorte = texto_derecha(entrada, imag, colorT)
        print(alin)
    #print(type(evento_string))
    #comparaciones(evento_string)    
def callback12(event):
    print("entro al 12")
    print(alin)
    if(alin == "centrar()"):
        guardar_imagen(imgCorte)
    elif(alin == "arriba()"):
        guardar_imagen(imgCorte)
    elif(alin == "abajo()"):
        guardar_imagen(imgCorte)
    elif(alin == "texto_izquierda()"):
        guardar_imagen(imgCorte)
    elif(alin == "texto_derecha()"):
        guardar_imagen(imgCorte)        
        
def centrar(entrada, imag, colorT):    
    print(entrada)
    print(colorT)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))
    print(texto)
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 200), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)      
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final                  
                     
def arriba(entrada, imag, colorT):    
    print(entrada)
    print(colorT)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))       
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 10), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)      
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final                  

def abajo(entrada, imag, colorT):    
    print(entrada)
    print(colorT)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))
    print(texto)    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((150, 350), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)      
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final                  

def texto_derecha(entrada, imag, colorT):    
    print(entrada)
    print(colorT)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((290, 200), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)      
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final   

def texto_izquierda(entrada, imag, colorT):    
    print(entrada)
    print(colorT)
    imag = imag.convert("RGBA")
    texto = Image.new('RGBA', imag.size, (255,255,255,0))    
    fuente = ImageFont.truetype("Ubuntu-B.ttf", 25)
    dibujo = ImageDraw.Draw(texto)
    dibujo.text((10, 200), entrada, font=fuente, fill=colorT)    
    final = Image.alpha_composite(imag, texto)      
    image1 = ImageTk.PhotoImage(final)
    background_label = Label(pantallaAlineacion, image=image1)
    background_label.image=image1
    background_label.place(x=0, y=60, height=385, width=400) 
    return final                              
                 
if __name__ == '__main__':
    main()
    
    
