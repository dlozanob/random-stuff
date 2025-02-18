from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
import time
import os  # Used to run main.py

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
_location = os.path.dirname(__file__)
ASSETS_PATH = OUTPUT_PATH / Path(r"{0}/assets/frame8".format(_location))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


splash = Tk()
splash.title("Splash Screen")
#splash.geometry("505x258")

window_width = 700
window_height = 385
# Get screen width and height
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

# Calculate position (x, y) for the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set geometry and position
splash.geometry(f"{window_width}x{window_height}+{x}+{y}")

splash.overrideredirect(True)
splash.configure(bg = "#FFFFFF")

canvas = Canvas(
    splash,
    bg = "#FFFFFF",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350,
    192,
    image=image_image_1
)

# Function to open main application
def open_main():
    splash.destroy()  # Close splash screen
    main_path = '{0}/GUI.py'.format(_location)
    os.system('python "{0}"'.format(main_path))  # Run main.py (Change to "python3" for macOS/Linux)

# Keep splash screen for 3 seconds
splash.after(3000, open_main)

splash.resizable(False, False)
splash.mainloop()
