# random-stuff

For cheatsheets: https://cheatsheets-editor.com/

import tkinter as tk

# Variable para verificar si la tecla está presionada
key_pressed = False

def on_key_press(event):
    global key_pressed
    if not key_pressed:  # Verificar si la tecla aún no está siendo procesada
        print(1)  # Acción cuando la tecla se presiona por primera vez
        key_pressed = True
        repeat_action()

def on_key_release(event):
    global key_pressed
    if key_pressed:  # Verificar si la tecla estaba presionada
        print(0)  # Acción cuando la tecla es liberada
        key_pressed = False
        root.after_cancel(repeat_id)

def repeat_action():
    # Realiza la acción repetida mientras la tecla esté presionada
    if key_pressed:
        print(1)  # Continuar con la acción mientras la tecla esté presionada
        global repeat_id
        repeat_id = root.after(100, repeat_action)  # Llamar a repeat_action nuevamente después de 100 ms

# Crear la ventana principal
root = tk.Tk()
root.title("Detectar evento mientras se oprime la flecha izquierda")

# Asociar los eventos de teclas
root.bind("<KeyPress-Left>", on_key_press)  # Detectar cuando la tecla se empieza a presionar (KeyPress)
root.bind("<KeyRelease-Left>", on_key_release)  # Detectar cuando se libera la flecha izquierda

# Iniciar el bucle principal de la interfaz
root.mainloop()
