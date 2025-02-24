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
from assets1 import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import threading
import support

from DualCameraWindow import *
from Actuators import *

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
	try: support.root.tk.call('source',
				os.path.join(_location, 'themes', 'default.tcl'))
	except: pass
	style = ttk.Style()
	style.theme_use('default')
	style.configure('.', font = "TkDefaultFont")
	if sys.platform == "win32":
		style.theme_use('winnative')    
	_style_code_ran = 1

class GUI:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		top is the toplevel containing window.'''

		self.top = top

		#self.top.update_idletasks() # Update Window Info
		#top_width = top.winfo_width()
		#top_height = top.winfo_height()

		self.top_width = top.winfo_screenwidth()
		self.top_height = top.winfo_screenheight()

		#top.wm_attributes("-zoomed", True)
		self.top.geometry("{0}x{1}+{2}+{3}".format(self.top_width//4, self.top_height-50, 3*self.top_width//4, 0))

		self.camera_posx = ceil(self.top_width*0.028) # Given in pixels
		self.camera_posy = ceil(self.top_height*0.122) # Given in pixels
		self.camera_width = ceil(self.top_width*(0.718/2)) # Given in pixels
		self.camera_height = ceil(self.top_height*(0.836)) # Given in pixels

		self.top.minsize(120, 1)
		self.top.resizable(1,  1)
		self.top.title("Smart Aligner")
		self.top.configure(background="#d9d9d9")
		self.top.configure(highlightbackground="#d9d9d9")
		self.top.configure(highlightcolor="#000000")

		self.top.bind("<Left>", self.move_left_safe)
		self.top.bind("<Right>", self.move_right_safe)
		self.top.bind("<Up>", self.detect_key)
		self.top.bind("<Down>", self.detect_key)
		self.top.bind("a", self.detect_key)
		self.top.bind("d", self.detect_key)
		self.top.bind("g", self.detect_key)
		self.top.bind("<Enter>", self.send_displacement)
		self.top.bind("<Escape>", self.detect_key)

		self.obj_pos_x = 0.1
		self.obj_width = 0.8 

		self.left_cam_state = 1
		self.right_cam_state = 1
		self.grid = 1
		self.alternate_rate = 1
		self.alternate_counter = 0
		self.button_cam_def_img = ImageTk.PhotoImage(Image.open(button_cam_def_path))
		self.button_camOff_def_img = ImageTk.PhotoImage(Image.open(button_camOff_def_path))
		self.button_left_def_img = ImageTk.PhotoImage(Image.open(button_left_def_path))
		self.button_right_def_img = ImageTk.PhotoImage(Image.open(button_right_def_path))
		self.img_cameraOff_img = ImageTk.PhotoImage(Image.open(img_cameraOff_path))
		self.button_grid_def_img = ImageTk.PhotoImage(Image.open(button_grid_def_path))

		self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		self.top.configure(menu = self.menubar)

		self.Labelframe1 = tk.LabelFrame(self.top)
		self.Labelframe1.place(relx=self.obj_pos_x, rely=0.546, relheight=0.26
			, relwidth=self.obj_width)
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
		self.Button4.bind("<ButtonPress>", lambda event: self.toggle_left_cam(event))

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
		self.Button5.bind("<ButtonPress>", lambda event: self.toggle_right_cam(event))

		self.Labelframe3 = tk.LabelFrame(self.Labelframe1)
		self.Labelframe3.place(relx=0.091, rely=0.534, relheight=0.414
			, relwidth=0.864, bordermode='ignore')
		self.Labelframe3.configure(relief='groove')
		self.Labelframe3.configure(foreground="#000000")
		self.Labelframe3.configure(text='''Zoom''')
		self.Labelframe3.configure(background="#d9d9d9")
		self.Labelframe3.configure(highlightbackground="#d9d9d9")
		self.Labelframe3.configure(highlightcolor="#000000")

		self.Scale1 =  tk.Scale(self.Labelframe3, from_=1.0, to=5.0, resolution=1.0, command=self.on_zoom_change)
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
		self.Frame1.place(relx=self.obj_pos_x, rely=0.830, relheight=0.114
			, relwidth=self.obj_width)
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
		self.Button11.bind("<ButtonRelease>", self.salir)

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
		self.Button3.configure(text='''Controles''')
		self.Button3.bind("<ButtonPress>", self.show_instructions)

		self.Label1 = tk.Label(self.top)
		self.Label1.place(relx=self.obj_pos_x - 0.08, rely=0.02, height=67, width=358)
		self.Label1.configure(activebackground="#d9d9d9")
		self.Label1.configure(activeforeground="black")
		self.Label1.configure(background="#d9d9d9")
		self.Label1.configure(compound='left')
		self.Label1.configure(disabledforeground="#a3a3a3")
		self.Label1.configure(font="-family {Romantic} -size 12 -weight bold")
		self.Label1.configure(foreground="#000000")
		self.Label1.configure(highlightbackground="#d9d9d9")
		self.Label1.configure(highlightcolor="#000000")
		self.Label1.configure(text='''SMART ALIGNER''')

		self.Button6 = tk.Button(self.top)
		self.Button6.place(relx=self.obj_pos_x, rely=0.027, height=56, width=57)
		self.Button6.configure(activebackground="#d9d9d9")
		self.Button6.configure(activeforeground="black")
		self.Button6.configure(background="#d9d9d9")
		self.Button6.configure(disabledforeground="#a3a3a3")
		self.Button6.configure(foreground="#000000")
		self.Button6.configure(highlightbackground="#d9d9d9")
		self.Button6.configure(highlightcolor="#000000")
		self.Button6.configure(image=self.button_grid_def_img)
		self.Button6.configure(cursor="hand2")
		self.Button6.bind("<ButtonPress>", self.toggle_grid)

		self.Labelframe5 = tk.LabelFrame(self.top)
		self.Labelframe5.place(relx=self.obj_pos_x, rely=0.122, relheight=0.408
			, relwidth=self.obj_width)
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
		self.Button8.bind("<ButtonPress>", self.move_left)
		self.Button8.bind("<ButtonRelease>", self.move_left_stop)

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
		self.Button9.bind("<ButtonPress>", self.move_right)
		self.Button9.bind("<ButtonRelease>", self.move_right_stop)

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
		self.Button10.bind("<ButtonPress>", self.send_displacement)


		## INITIALIZING CAMERAS ##
		
		self.dualCamWin = DualCameraWindow(win_width=3*self.top_width//4)
		cam_thread = threading.Thread(target=self.dualCamWin.initialize)
		cam_thread.start()

		## INITIALIZING ACTUATORS ##
		self.actuator_control = Actuator_Control()
		self.actuator_control.motor1_activo = True
		self.actuator_control.motor2_activo = True

		self.repeat_id1 = None
		self.repeat_id2 = None

	#### FUNCIONES BOTONES ####
	def salir(self, event):
		time.sleep(0.2)
		#self.dualCamWin.set_terminate(1)
		self.top.destroy()

	def send_displacement(self, event):
		try:
			valor = int(self.Entry2.get())  # Obtener el valor del Entry y convertir a entero
			valor *= 10 # mm
			paso = self.actuator_control.calcular_pasos(valor)
			

			if 0 <= valor <= 200:
				print(f"Valor ingresado: {valor}")  # Imprimir si es válido
				actuator_mode = self.Scale2.get()
				if(actuator_mode == 0):
					# ACTUADOR 1
					self.actuator_control.set_dir(1)
					self.actuator_control.controlar_motor(1)
					self.actuator_control.set_dir(0)
					self.actuator_control.mover_motores(paso,1)

					pass
				elif(actuator_mode == 1):
					# AMBOS ACTUADORES				
					self.actuator_control.set_dir(1)		
					self.actuator_control.controlar_motor(1)
					self.actuator_control.controlar_motor(2)
					self.actuator_control.set_dir(0)
					self.actuator_control.mover_motores(paso,1)
					self.actuator_control.mover_motores(paso,2)
				else:
					# ACTUADOR 2
					self.actuator_control.set_dir(1)
					self.actuator_control.controlar_motor(2)
					self.actuator_control.set_dir(0)
					self.actuator_control.mover_motores(paso,2)
					pass  
			else:
				messagebox.showwarning("Advertencia", "El número debe estar entre 1 y 20.")  # Mostrar advertencia

		except ValueError:
			messagebox.showwarning("Advertencia", "No es posible mover los motores. Esto puede deberse a un error de conexión.")
			self.Entry2.delete(0, 'end')

	def toggle_left_cam(self, event):
		if (self.left_cam_state):
			##APAGAR CÁMARA IZQUIERDA##
			self.Button4.configure(image=self.button_camOff_def_img)
			self.dualCamWin.set_cam_0_on(0)              
		else:
			##PRENDER CÁMARA IZQUIERDA##
			self.Button4.configure(image=self.button_cam_def_img)
			self.dualCamWin.set_cam_0_on(1)   
		self.left_cam_state = not self.left_cam_state

	def toggle_right_cam(self, event):
		if (self.right_cam_state):
			##APAGAR CÁMARA DERECHA##
			self.Button5.configure(image=self.button_camOff_def_img)
			self.dualCamWin.set_cam_1_on(0)
		else:
			##PRENDER CÁMARA DERECHA##
			self.Button5.configure(image=self.button_cam_def_img)
			self.dualCamWin.set_cam_1_on(1)
		self.right_cam_state = not self.right_cam_state

	def on_zoom_change(self, event):
		self.dualCamWin.set_zoom_factor(self.Scale1.get())

	def move_left_safe(self, event):
		actuator_mode = self.Scale2.get()
		paso = self.actuator_control.calcular_pasos(5)
		
		if(actuator_mode == 0):
			# ACTUADOR 1
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,1)
		elif(actuator_mode == 1):
			# AMBOS ACTUADORES
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,1)
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,2)			
		else:
			# ACTUADOR 2
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,2)

	def move_right_safe(self, event):
		actuator_mode = self.Scale2.get()
		paso = self.actuator_control.calcular_pasos(5)

		if(actuator_mode == 0):
			# ACTUADOR 1
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,1)
		elif(actuator_mode == 1):
			# AMBOS ACTUADORES
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,1)
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,2)			
		else:
			# ACTUADOR 2
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,2)    

	def move_left(self, event):
		self.move_left_action()			

	def move_left_action(self):
		actuator_mode = self.Scale2.get()
		paso = self.actuator_control.calcular_pasos(5)
		
		if(actuator_mode == 0):
			# ACTUADOR 1
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,1)
		elif(actuator_mode == 1):
			# AMBOS ACTUADORES
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,1)
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,2)			
		else:
			# ACTUADOR 2
			self.actuator_control.set_dir(0)
			self.actuator_control.mover_motores(paso,2)
		self.repeat_id1 = self.top.after(50, self.move_left_action)

	def move_left_stop(self, event):
		self.top.after_cancel(self.repeat_id1)

	def move_right(self, event):
		self.move_right_action()

	def move_right_action(self):
		actuator_mode = self.Scale2.get()
		paso = self.actuator_control.calcular_pasos(5)

		if(actuator_mode == 0):
			# ACTUADOR 1
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,1)
		elif(actuator_mode == 1):
			# AMBOS ACTUADORES
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,1)
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,2)			
		else:
			# ACTUADOR 2
			self.actuator_control.set_dir(1)
			self.actuator_control.mover_motores(paso,2)    

		self.repeat_id2 = self.top.after(100, self.move_right_action)

	def move_right_stop(self, event):
		self.top.after_cancel(self.repeat_id2)

	def toggle_grid(self, event):
		if(self.grid):
			self.dualCamWin.set_grid_on(0)
		else:
			self.dualCamWin.set_grid_on(1)
		self.grid = not self.grid

	def detect_key(self, event):
		zoom_scale = self.Scale1.get()

		if event.keysym == "Up":
			if zoom_scale < 5:
				self.Scale1.set(zoom_scale + 1)
		elif event.keysym == "Down":
			if zoom_scale > 1:
				self.Scale1.set(zoom_scale - 1)
		elif event.keysym == "a":
			self.toggle_left_cam(event)
		elif event.keysym == "d":
			self.toggle_right_cam(event)
		elif event.keysym == "g":
			self.toggle_grid(event)
		elif event.keysym == "Enter":
			self.send_displacement(event)
		elif event.keysym == "Escape":
			self.salir(event)
		print(self.Scale1.get())

	def show_instructions(self, event):
		main_path = '{0}/instructions.py'.format(_location)
		os.system('python "{0}"'.format(main_path))
	########## FIN ############

if __name__ == '__main__':
	'''Main entry point for the application.'''
	global root
	root = tk.Tk()
	root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
	# Creates a toplevel widget.
	global _top, _w
	_top = root
	_w = GUI(_top)
	root.mainloop()

