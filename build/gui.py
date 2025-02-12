from pathlib import Path
import os
from PIL import Image, ImageTk  # Install Pillow: pip install pillow

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#from assets1 import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USUARIO\Desktop\Letztes Semester\Proyecto Aplicado de Ingeniería\Proyecto\Application\Code\Build\build\assets\frame0")
_location = os.path.dirname(__file__)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Smart Aligner")
window.attributes('-fullscreen',True)

# width= window.winfo_screenwidth()               
# height= window.winfo_screenheight()               
# window.geometry("%dx%d" % (width, height))
#window.geometry("775x542")
window.configure(bg = "#CDC2C2")
window.state('zoomed')


#######################################################################################################################

button_grid_def = ImageTk.PhotoImage(Image.open("{0}/assets/Grid/button_1.png".format(_location)))
button_grid_def = ImageTk.PhotoImage(Image.open("{0}/assets/Grid/button_1.png".format(_location)))
button_grid_hover = ImageTk.PhotoImage(Image.open("{0}/assets/Grid/button_2.png".format(_location)))
button_grid_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/Grid/button_3.png".format(_location)))
button_ins_def = ImageTk.PhotoImage(Image.open("{0}/assets/Ins/button_1.png".format(_location)))
button_ins_hover = ImageTk.PhotoImage(Image.open("{0}/assets/Ins/button_2.png".format(_location)))
button_ins_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/Ins/button_3.png".format(_location)))
button_man_def = ImageTk.PhotoImage(Image.open("{0}/assets/Manual/button_1.png".format(_location)))
button_man_hover = ImageTk.PhotoImage(Image.open("{0}/assets/Manual/button_2.png".format(_location)))
button_man_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/Manual/button_3.png".format(_location)))
button_cam_def = ImageTk.PhotoImage(Image.open("{0}/assets/Camera/button_1.png".format(_location)))
button_cam_hover = ImageTk.PhotoImage(Image.open("{0}/assets/Camera/button_2.png".format(_location)))
button_cam_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/Camera/button_3.png".format(_location)))
button_home_def = ImageTk.PhotoImage(Image.open("{0}/assets/Home/button_1.png".format(_location)))
button_home_hover = ImageTk.PhotoImage(Image.open("{0}/assets/Home/button_2.png".format(_location)))
button_home_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/Home/button_3.png".format(_location)))
button_left_def = ImageTk.PhotoImage(Image.open("{0}/assets/LeftArrow/button_1.png".format(_location)))
button_left_hover = ImageTk.PhotoImage(Image.open("{0}/assets/LeftArrow/button_2.png".format(_location)))
button_left_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/LeftArrow/button_3.png".format(_location)))
button_right_def = ImageTk.PhotoImage(Image.open("{0}/assets/RightArrow/button_1.png".format(_location)))
button_right_hover = ImageTk.PhotoImage(Image.open("{0}/assets/RightArrow/button_2.png".format(_location)))
button_right_pressed = ImageTk.PhotoImage(Image.open("{0}/assets/RightArrow/button_3.png".format(_location)))

#######################################################################################################################

def on_hover(event):
    button = event.widget
    if button == button_1:
        button_1.config(image=button_grid_hover)
    elif button == button_2:
        button_2.config(image=button_ins_hover)    
    elif button == button_3:
        button_3.config(image=button_man_hover)
    elif button == button_4:
        button_4.config(image=button_cam_hover)
    elif button == button_5:
        button_5.config(image=button_cam_hover)
    elif button == button_6:
        button_6.config(image=button_home_hover)
    elif button == button_7:
        button_7.config(image=button_right_hover)  
    elif button == button_8:
        button_8.config(image=button_left_hover)
    elif button == button_9:
        button_9.config(image=button_home_hover)
    elif button == button_10:
        button_10.config(image=button_right_hover)
    elif button == button_11:
        button_11.config(image=button_left_hover)
                         
    
def on_leave(event):
    button = event.widget    
    if button == button_1:
        button_1.config(image=button_grid_def)
    elif button == button_2:
        button_2.config(image=button_ins_def)      
    elif button == button_3:
        button_3.config(image=button_man_def)
    elif button == button_4:
        button_4.config(image=button_cam_def)
    elif button == button_5:
        button_5.config(image=button_cam_def)
    elif button == button_6:
        button_6.config(image=button_home_def)
    elif button == button_7:
        button_7.config(image=button_right_def)    
    elif button == button_8:
        button_8.config(image=button_left_def)
    elif button == button_9:
        button_9.config(image=button_home_def)
    elif button == button_10:
        button_10.config(image=button_right_def)
    elif button == button_11:
        button_11.config(image=button_left_def)

def on_press(event):
    button = event.widget    
    if button == button_1:
        button_1.config(image=button_grid_pressed)
    elif button == button_2:
        button_2.config(image=button_ins_pressed)      
    elif button == button_3:
        button_3.config(image=button_man_pressed)
    elif button == button_4:
        button_4.config(image=button_cam_pressed)
    elif button == button_5:
        button_5.config(image=button_cam_pressed)
    elif button == button_6:
        button_6.config(image=button_home_pressed)
    elif button == button_7:
        button_7.config(image=button_right_pressed)    
    elif button == button_8:
        button_8.config(image=button_left_pressed)
    elif button == button_9:
        button_9.config(image=button_home_pressed)
    elif button == button_10:
        button_10.config(image=button_right_pressed)
    elif button == button_11:
        button_11.config(image=button_left_pressed)

#######################################################################################################################

canvas = Canvas(
    window,
    bg = "#CDC2C2",
    height = 542,
    width = 775,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    140.0,
    119.0,
    660.0,
    363.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    284.0,
    23.0,
    anchor="nw",
    text="Smart Aligner",
    fill="#000000",
    font=("JetBrainsMono Bold", 32 * -1)
)


#######################################################################################################################

button_1 = Button(
    image=button_grid_def,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

button_1.place(
    x=42.0,
    y=241.0,
    width=48.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=14.0,
    y=16.0,
    width=118.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=14.0,
    y=60.0,
    width=149.0,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(
    636.0,
    462.0,
    image=image_image_1
)

canvas.create_text(
    600.0,
    405.0,
    anchor="nw",
    text="Cámaras",
    fill="#000000",
    font=("Inter ExtraBold", 16 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=572.0,
    y=447.0,
    width=52.0,
    height=53.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=651.0,
    y=447.0,
    width=52.0,
    height=53.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    636.0,
    467.0,
    image=image_image_2
)

canvas.create_text(
    593.0,
    423.0,
    anchor="nw",
    text="L",
    fill="#9A8A8A",
    font=("Inter ExtraBold", 16 * -1)
)

canvas.create_text(
    671.0,
    423.0,
    anchor="nw",
    text="R",
    fill="#9A8A8A",
    font=("Inter ExtraBold", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    410.0,
    462.0,
    image=image_image_3
)

canvas.create_text(
    370.0,
    409.0,
    anchor="nw",
    text="Actuador 2",
    fill="#000000",
    font=("Inter ExtraBold", 16 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=329.0,
    y=446.0,
    width=56.0,
    height=50.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=449.0,
    y=446.0,
    width=48.0,
    height=48.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=393.0,
    y=446.0,
    width=48.0,
    height=48.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    174.0,
    462.0,
    image=image_image_4
)

canvas.create_text(
    134.0,
    409.0,
    anchor="nw",
    text="Actuador 1",
    fill="#000000",
    font=("Inter ExtraBold", 16 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=93.0,
    y=446.0,
    width=56.0,
    height=50.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=213.0,
    y=446.0,
    width=48.0,
    height=48.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=157.0,
    y=447.0,
    width=48.0,
    height=48.0
)

button_12 = Button(
    borderwidth = 0,
    highlightthickness= 0,
    command = lambda: print("button_12 clicked"),
    relief = "flat"
)
button_12.place(
    x=157.0,
    y=447.0,
    width=48.0,
    height=48.0
)


#######################################################################################################################

button_1.bind("<Enter>", on_hover)
button_1.bind("<Leave>", on_leave)
button_1.bind("<ButtonPress>", on_press)
button_2.bind("<Enter>", on_hover)
button_2.bind("<Leave>", on_leave)
button_2.bind("<ButtonPress>", on_press)
button_3.bind("<Enter>", on_hover)
button_3.bind("<Leave>", on_leave)
button_3.bind("<ButtonPress>", on_press)
button_4.bind("<Enter>", on_hover)
button_4.bind("<Leave>", on_leave)
button_4.bind("<ButtonPress>", on_press)
button_5.bind("<Enter>", on_hover)
button_5.bind("<Leave>", on_leave)
button_5.bind("<ButtonPress>", on_press)
button_6.bind("<Enter>", on_hover)
button_6.bind("<Leave>", on_leave)
button_6.bind("<ButtonPress>", on_press)
button_7.bind("<Enter>", on_hover)
button_7.bind("<Leave>", on_leave)
button_7.bind("<ButtonPress>", on_press)
button_8.bind("<Enter>", on_hover)
button_8.bind("<Leave>", on_leave)
button_8.bind("<ButtonPress>", on_press)
button_9.bind("<Enter>", on_hover)
button_9.bind("<Leave>", on_leave)
button_9.bind("<ButtonPress>", on_press)
button_10.bind("<Enter>", on_hover)
button_10.bind("<Leave>", on_leave)
button_10.bind("<ButtonPress>", on_press)
button_11.bind("<Enter>", on_hover)
button_11.bind("<Leave>", on_leave)
button_11.bind("<ButtonPress>", on_press)

#######################################################################################################################

window.mainloop()
