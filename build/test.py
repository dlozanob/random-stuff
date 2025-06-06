#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Feb 12, 2025 12:31:55 AM EST  platform: Windows NT

import sys
import time
from math import *
import numpy as np
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from PIL import Image, ImageTk
import cv2
import test1_support
from assets1 import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: test1_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    
    _style_code_ran = 1

class Toplevel3:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        #top.geometry("1064x736+1771+146")
        #top.state('zoomed')
        top.wm_attributes("-zoomed", True)
        top.update_idletasks() # Update Window Info
        top_width = top.winfo_width()
        top_height = top.winfo_height()

        top.minsize(120, 1)
        #top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Toplevel 1")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.left_cam_state = 1
        self.right_cam_state = 1
        self.grid = 1
        self.button_cam_def_img = ImageTk.PhotoImage(Image.open(button_cam_def_path))
        self.button_camOff_def_img = ImageTk.PhotoImage(Image.open(button_camOff_def_path))
        self.button_left_def_img = ImageTk.PhotoImage(Image.open(button_left_def_path))
        self.button_right_def_img = ImageTk.PhotoImage(Image.open(button_right_def_path))
        self.img_cameraOff_img = ImageTk.PhotoImage(Image.open(img_cameraOff_path))
        self.button_grid_def_img = ImageTk.PhotoImage(Image.open(button_grid_def_path))

        #### FUNCIONES BOTONES ####
        def salir(event):
            time.sleep(0.2)
            self.top.destroy()

        def send_displacement(event, entry):
            try:
                valor = int(entry.get())  # Obtener el valor del Entry y convertir a entero
                
                if 0 <= valor <= 40:
                    print(f"Valor ingresado: {valor}")  # Imprimir si es válido
                    actuator_mode = self.Scale2.get()
                    if(actuator_mode == 0):
                        # ACTUADOR 1
                        pass
                    elif(actuator_mode == 1):
                        # AMBOS ACTUADORES
                        pass
                    else:
                        # ACTUADOR 2
                        pass  
                else:
                    messagebox.showwarning("Advertencia", "El número debe estar entre 1 y 40.")  # Mostrar advertencia

            except ValueError:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un número entero entre 0 y 40.")
                entry.delete(0, 'end')

        def toggle_left_cam(event, btn, cam):
            if (self.left_cam_state):
                ##APAGAR CÁMARA IZQUIERDA##
                self.left_cam_state = 0
                btn.configure(image=self.button_camOff_def_img)                
            else:
                ##PRENDER CÁMARA IZQUIERDA##
                self.left_cam_state = 1
                self.update_frame1()
                btn.configure(image=self.button_cam_def_img)
            print("Left cam toggled")

        def toggle_right_cam(event, btn, cam):
            if (self.right_cam_state):
                ##APAGAR CÁMARA DERECHA##
                self.right_cam_state = 0
                btn.configure(image=self.button_camOff_def_img)
                
            else:
                ##PRENDER CÁMARA DERECHA##
                self.right_cam_state = 1
                self.update_frame2()
                btn.configure(image=self.button_cam_def_img)
            print("Right cam toggled")

        def move_left(event, scale):
            actuator_mode = scale.get()
            if(actuator_mode == 0):
                # ACTUADOR 1
                pass
            elif(actuator_mode == 1):
                # AMBOS ACTUADORES
                pass
            else:
                # ACTUADOR 2
                pass
            print("Moving to left")

        def move_right(event, scale):
            actuator_mode = scale.get()
            if(actuator_mode == 0):
                # ACTUADOR 1
                pass
            elif(actuator_mode == 1):
                # AMBOS ACTUADORES
                pass
            else:
                # ACTUADOR 2
                pass            
            print("Moving to right")

        def toggle_grid(event):
            if(self.grid):
                self.grid = 0
            else:
                self.grid = 1

        ########## FIN ############

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.761, rely=0.546, relheight=0.26
                , relwidth=0.207)
        self.Labelframe1.configure(relief='sunken')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 9")
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(relief="sunken")
        self.Labelframe1.configure(text='''Cámaras''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="#000000")

        _style_code()
        self.TSeparator1 = ttk.Separator(self.Labelframe1)
        self.TSeparator1.place(relx=0.529, rely=0.178, relheight=0.518
                , bordermode='ignore')
        self.TSeparator1.configure(orient="vertical")

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.210, rely=0.065, height=31, width=34
                , bordermode='ignore')
        self.Label5.configure(activebackground="#d9d9d9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 18")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="#000000")
        self.Label5.configure(text='''L''')

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.684, rely=0.065, height=30, width=33
                , bordermode='ignore')
        self.Label6.configure(activebackground="#d9d9d9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 18")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="#000000")
        self.Label6.configure(text='''R''')

        self.Button4 = tk.Button(self.Labelframe1)
        self.Button4.place(relx=0.182, rely=0.222, height=57, width=57
                , bordermode='ignore')  
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 9")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="#000000")
        self.Button4.configure(text='''Button''')        
        self.Button4.configure(image=self.button_cam_def_img)
        self.Button4.configure(cursor="hand2")
        self.Button4.bind("<ButtonPress>", lambda event: toggle_left_cam(event, self.Button4, self.camera1))

        self.Button5 = tk.Button(self.Labelframe1)
        self.Button5.place(relx=0.636, rely=0.222, height=57, width=57
                , bordermode='ignore')
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="black")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(cursor="arrow")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Segoe UI} -size 9")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="#000000")
        self.Button5.configure(text='''Button''')
        self.Button5.configure(image=self.button_cam_def_img)
        self.Button5.configure(cursor="hand2")
        self.Button5.bind("<ButtonPress>", lambda event: toggle_right_cam(event, self.Button5, self.camera2))

        self.Labelframe3 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe3.place(relx=0.091, rely=0.534, relheight=0.414
                , relwidth=0.864, bordermode='ignore')
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''Zoom''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="#000000")

        self.Scale1 =  tk.Scale(self.Labelframe3, from_=1.0, to=5.0, resolution=1.0)
        self.Scale1.place(relx=0.053, rely=0.042, relheight=0.733
                , relwidth=0.874)
        self.Scale1.configure(activebackground="#d9d9d9")
        self.Scale1.configure(background="#d9d9d9")
        self.Scale1.configure(foreground="#000000")
        self.Scale1.configure(highlightbackground="#d9d9d9")
        self.Scale1.configure(highlightcolor="#000000")
        self.Scale1.configure(length="166")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="#c4c4c4")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.761, rely=0.830, relheight=0.114
                , relwidth=0.209)
        self.Frame1.configure(relief='sunken')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="sunken")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Button11 = tk.Button(self.Frame1)
        self.Button11.place(relx=0.59, rely=0.298, height=36, width=67)
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(activeforeground="black")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="#000000")
        self.Button11.configure(text='''Salir''')
        self.Button11.configure(cursor="hand2")
        self.Button11.bind("<ButtonRelease>", salir)

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.09, rely=0.298, height=36, width=87)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(cursor="arrow")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(text='''Instrucciones''')

        self.Button6 = tk.Button(self.top)
        self.Button6.place(relx=0.028, rely=0.027, height=56, width=57)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="black")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="#000000")
        self.Button6.configure(image=self.button_grid_def_img)
        self.Button6.configure(cursor="hand2")
        self.Button6.bind("<ButtonPress>", toggle_grid)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.273, rely=0.014, height=67, width=358)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Romantic} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''SMART ALIGNER''')

        self.Labelframe5 = tk.LabelFrame(self.top)
        self.Labelframe5.place(relx=0.761, rely=0.122, relheight=0.408
                , relwidth=0.207)
        self.Labelframe5.configure(relief='sunken')
        self.Labelframe5.configure(font="-family {Segoe UI} -size 9")
        self.Labelframe5.configure(foreground="#000000")
        self.Labelframe5.configure(relief="sunken")
        self.Labelframe5.configure(text='''Actuadores''')
        self.Labelframe5.configure(background="#d9d9d9")
        self.Labelframe5.configure(cursor="arrow")
        self.Labelframe5.configure(highlightbackground="#d9d9d9")
        self.Labelframe5.configure(highlightcolor="#000000")

        self.Label7 = tk.Label(self.Labelframe5)
        self.Label7.place(relx=0.091, rely=0.1, height=20, width=53
                , bordermode='ignore')
        self.Label7.configure(activebackground="#d9d9d9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 9")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="#000000")
        self.Label7.configure(text='''Izquierdo''')

        self.Label8 = tk.Label(self.Labelframe5)
        self.Label8.place(relx=0.4, rely=0.1, height=20, width=44
                , bordermode='ignore')
        self.Label8.configure(activebackground="#d9d9d9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 9")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="#000000")
        self.Label8.configure(text='''Ambos''')

        self.Label9 = tk.Label(self.Labelframe5)
        self.Label9.place(relx=0.668, rely=0.1, height=20, width=63
                , bordermode='ignore')
        self.Label9.configure(activebackground="#d9d9d9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 9")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="#000000")
        self.Label9.configure(text='''Derecho''')

        self.Labelframe7 = tk.LabelFrame(self.Labelframe5)
        self.Labelframe7.place(relx=0.045, rely=0.333, relheight=0.343
                , relwidth=0.909, bordermode='ignore')
        self.Labelframe7.configure(relief='groove')
        self.Labelframe7.configure(font="-family {Segoe UI} -size 9")
        self.Labelframe7.configure(foreground="#000000")
        self.Labelframe7.configure(text='''Manual''')
        self.Labelframe7.configure(background="#d9d9d9")
        self.Labelframe7.configure(highlightbackground="#d9d9d9")
        self.Labelframe7.configure(highlightcolor="#000000")

        self.Button8 = tk.Button(self.Labelframe7)
        self.Button8.place(relx=0.15, rely=0.291, height=57, width=57
                , bordermode='ignore')
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="black")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="#000000")
        self.Button8.configure(text='''Button''')
        self.Button8.configure(image=self.button_left_def_img)
        self.Button8.configure(cursor="hand2")
        self.Button8.bind("<ButtonPress>", lambda event: move_left(event, self.Scale2))

        self.Button9 = tk.Button(self.Labelframe7)
        self.Button9.place(relx=0.55, rely=0.291, height=57, width=57
                , bordermode='ignore')
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="black")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="#000000")
        self.Button9.configure(text='''Button''')
        self.Button9.configure(image=self.button_right_def_img)
        self.Button9.configure(cursor="hand2")
        self.Button9.bind("<ButtonPress>", lambda event: move_right(event, self.Scale2))

        self.Scale2 =  tk.Scale(self.Labelframe5, from_=0.0, to=2.0, resolution=1.0)
        self.Scale2.place(relx=0.091, rely=0.14, relheight=0.1, relwidth=0.85)
        self.Scale2.configure(activebackground="#d9d9d9")
        self.Scale2.configure(background="#d9d9d9")
        self.Scale2.configure(font="-family {Segoe UI} -size 9")
        self.Scale2.configure(foreground="#000000")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="#000000")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(showvalue="0")
        self.Scale2.configure(troughcolor="#c4c4c4")

        self.Labelframe6 = tk.LabelFrame(self.Labelframe5)
        self.Labelframe6.place(relx=0.045, rely=0.7, relheight=0.24
                , relwidth=0.909, bordermode='ignore')
        self.Labelframe6.configure(relief='groove')
        self.Labelframe6.configure(font="-family {Segoe UI} -size 9")
        self.Labelframe6.configure(foreground="#000000")
        self.Labelframe6.configure(text='''Automático''')
        self.Labelframe6.configure(background="#d9d9d9")
        self.Labelframe6.configure(cursor="arrow")
        self.Labelframe6.configure(highlightbackground="#d9d9d9")
        self.Labelframe6.configure(highlightcolor="#000000")

        self.Entry2 = tk.Entry(self.Labelframe6)
        self.Entry2.place(relx=0.075, rely=0.417, height=20, relwidth=0.42
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="#000000")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#d9d9d9")
        self.Entry2.configure(selectforeground="black")

        self.Button10 = tk.Button(self.Labelframe6)
        self.Button10.place(relx=0.605, rely=0.403, height=26, width=67
                , bordermode='ignore')
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="black")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="#000000")
        self.Button10.configure(text='''Confirmar''')
        self.Button10.configure(cursor="hand2")
        self.Button10.bind("<ButtonPress>", lambda event: send_displacement(event, self.Entry2))

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.028, rely=0.122, relheight=0.836
                , relwidth=0.718)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="#000000")

        self.camera_posx = ceil(top_width*0.028) # Given in pixels
        self.camera_posy = ceil(top_height*0.122) # Given in pixels
        self.camera_width = ceil(top_width*(0.718/2)) # Given in pixels
        self.camera_height = ceil(top_height*(0.836)) # Given in pixels

        self.camera1 = tk.Label(self.top)
        self.camera1.place(x=self.camera_posx, y=self.camera_posy, width=self.camera_width, height=self.camera_height)
        self.camera1.configure(relief="groove")
        self.camera1.configure(background="#d9d9d9")
        self.camera1.configure(highlightbackground="#d9d9d9")
        self.camera1.configure(highlightcolor="#000000")

        self.camera2 = tk.Label(self.top)
        self.camera2.place(relx=0.028+0.718/2, rely=0.122, width=self.camera_width, height=self.camera_height)
        self.camera2.configure(relief="groove")
        self.camera2.configure(background="#d9d9d9")
        self.camera2.configure(highlightbackground="#d9d9d9")
        self.camera2.configure(highlightcolor="#000000")
        #self.camera2.configure(image=self.img_cameraOff_img)
        
        self.image_path1 = "/dev/shm/camera1.jpg"
        self.update_frame1()

        self.image_path2 = "/dev/shm/camera2.jpg"
        #self.update_frame2()

        ######CAM RPI 5######
        # INSTALAR: sudo apt install libopencv-dev python3-opencv
        # libcamera-jpeg -o test.jpg
        # SI NO FUNCIONA: sudo raspi-config
    #     self.image_path = "/dev/shm/camera.jpg"  # Usamos /dev/shm para evitar escribir en la SD
    #     self.update_frame()

    def capture_image1(self):
        """Captura una imagen usando libcamera-jpeg y la guarda en un archivo temporal."""
        os.system(f"libcamera-jpeg --camera 0 -o {self.image_path1} --width 640 --height 480 --nopreview -t 1")

    def update_frame1(self):
        """Captura un frame de la cámara y lo muestra en el Label."""
        self.capture_image1()  # Capturar nueva imagen

        if os.path.exists(self.image_path1):  # Verificar que la imagen existe
            img = Image.open(self.image_path1)
            img = img.resize((640, 480), Image.Resampling.LANCZOS)  # Redimensionar para la GUI
            img = np.array(img)
            
            zoom_factor = self.Scale1.get()
            
            # ###### Processing Image ######          
            img = self.zoom_image(img, zoom_factor)
            if(self.grid): img = self.add_cross(img, 2)
            img = Image.fromarray(img) # NumPy Array to PIL Image
            # ##############################
            
            imgtk = ImageTk.PhotoImage(image=img)

            # Mostrar en el Label
            self.camera1.imgtk = imgtk  # Evita que la imagen sea eliminada por el recolector de basura
            self.camera1.configure(image=imgtk)

        # Llamar a esta función cada 100 ms para actualizar la imagen
        if self.left_cam_state:
                self.top.after(10, self.update_frame1)
        else:
                self.camera1.configure(image=self.img_cameraOff_img)
                print("Camera Off")
        
                
    def capture_image2(self):
        """Captura una imagen usando libcamera-jpeg y la guarda en un archivo temporal."""
        os.system(f"libcamera-jpeg --camera 1 -o {self.image_path2} --width 640 --height 480 --nopreview -t 1")

    def update_frame2(self):
        """Captura un frame de la cámara y lo muestra en el Label."""
        self.capture_image2()  # Capturar nueva imagen

        if os.path.exists(self.image_path2):  # Verificar que la imagen existe
            img = Image.open(self.image_path2)
            img = img.resize((640, 480), Image.Resampling.LANCZOS)  # Redimensionar para la GUI
            img = np.array(img)
            
            zoom_factor = self.Scale1.get()
            
            # ###### Processing Image ######          
            img = self.zoom_image(img, zoom_factor)
            if(self.grid): img = self.add_cross(img, 2)
            img = Image.fromarray(img) # NumPy Array to PIL Image
            # ##############################
            
            imgtk = ImageTk.PhotoImage(image=img)

            # Mostrar en el Label
            self.camera2.imgtk = imgtk  # Evita que la imagen sea eliminada por el recolector de basura
            self.camera2.configure(image=imgtk)

        # Llamar a esta función cada 100 ms para actualizar la imagen
        if self.right_cam_state:
                self.top.after(100, self.update_frame2)
        else:
                self.camera2.configure(image=self.img_cameraOff_img)
                print("Camera Off")
        ########FIN##########

    # def update_frame(self):
        # """Captura un frame de la cámara y lo muestra en el Label."""
        # ret, frame = self.cap.read()
        # if ret:
            # # Convertir de BGR (OpenCV) a RGB (Tkinter)
            # #frame = cv2.resize(frame, (self.camera_width, self.camera_height)) # Resizing Camera Image
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # img = Image.fromarray(frame)
            # img = np.array(img) # Processing ONLY with cv2 (PIL Image to NumPy Array)

            # zoom_factor = self.Scale1.get()

            # ###### Processing Image ######          
            # img = self.zoom_image(img, zoom_factor)
            # if(self.grid): img = self.add_cross(img, 2)
            # img = Image.fromarray(img) # NumPy Array to PIL Image
            # ##############################

            # imgtk = ImageTk.PhotoImage(image=img)

            # # Mostrar en el Label
            # self.camera1.imgtk = imgtk  # Evita que la imagen sea eliminada por el recolector de basura
            # self.camera1.configure(image=imgtk)

        # # Llamar a esta función cada 10 ms
        # if self.left_cam_state:
            # self.top.after(10, self.update_frame)
        # else:
            # #self.camera.configure(image="")
            # self.camera1.configure(image=self.img_cameraOff_img)
            # print("Camera Off")

    ##########IMAGE PROCESSING#################
    def zoom_image(self, img, zoom_factor):
        h, w, _ = img.shape
        center_x, center_y = w//2, h//2

        new_w, new_h = int(w*zoom_factor), int(h*zoom_factor)
        resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
        
        # start_x = max(0, (new_w-w)//2)
        # start_y = max(0, (new_h-h)//2)

        start_x = max(0, (new_w-self.camera_width)//2)
        start_y = max(0, (new_h-self.camera_height)//2)

        if zoom_factor > 1:
            #zoomed_image = resized[start_y:, start_x:start_x + w]
            zoomed_image = resized[start_y : start_y + self.camera_height, start_x : start_x + self.camera_width]
        else:
            zoomed_image = np.zeros_like(img)
            zoomed_image[
                (h - new_h)//2 : (h-new_h)//2 + new_h,
                (w - new_w)//2 : (w - new_w)//2 + new_w
            ] = resized

        return zoomed_image

    def add_cross(self, img, thick):
        h, w, _ = img.shape
        modified_img = np.zeros_like(img)
        modified_img[:] = (0, 255, 0)

        modified_img[0 : h//2 - thick//2, 0 : w//2 - thick//2] = img[0 : h//2 - thick//2, 0 : w//2 - thick//2]
        modified_img[h//2 + thick//2 :, 0 : w//2 - thick//2] = img[h//2 + thick//2 :, 0 : w//2 - thick//2]
        modified_img[0 : h//2 - thick//2, w//2 + thick//2 :] = img[0 : h//2 - thick//2, w//2 + thick//2 :]
        modified_img[h//2 + thick//2 :, w//2 + thick//2 :] = img[h//2 + thick//2 :, w//2 + thick//2 :]

        return modified_img
    
    ###########################################


def start_up():
    test1_support.main()

if __name__ == '__main__':
    test1_support.main()
