# random-stuff

For cheatsheets: https://cheatsheets-editor.com/


from gpiozero import LED, Button
from time import sleep
import threading

# Definición de pines
DIR1 = LED(17)
STP1 = LED(27)
BTN1 = Button(5)
DIR2 = LED(23)
STP2 = LED(24)
BTN2 = Button(6)

# Variables de control
motor1_activo = False
motor2_activo = False
sentido1 = True  # Sentido antihorario
sentido2 = True  # Sentido antihorario

# Características físicas del motor
PULLEY_DIAMETER = 18  # mm
STEPS_PER_REV = 200
CIRCUMFERENCE = 3.1416 * PULLEY_DIAMETER
STEP_DISTANCE = CIRCUMFERENCE / STEPS_PER_REV  # mm por paso

# Hilos de control de los motores
motor1_thread = None
motor2_thread = None

# Eventos de detención para los hilos
motor1_stop_event = threading.Event()
motor2_stop_event = threading.Event()

def controlar_motor(k):
    global motor1_activo, sentido1, motor2_activo, sentido2
    motor_activo = motor1_activo if k == 1 else motor2_activo
    sentido = sentido1 if k == 1 else sentido2
    BTN = BTN1 if k == 1 else BTN2
    DIR = DIR1 if k == 1 else DIR2
    STP = STP1 if k == 1 else STP2
    stop_event = motor1_stop_event if k == 1 else motor2_stop_event

    while not stop_event.is_set():  # El hilo continuará hasta que se active la bandera de detención
        print(f"Motor {k} moviéndose en sentido antihorario hasta que se active el botón")

        DIR.value = 0  # Sentido antihorario
        tiempo_espera = 0
        while not BTN.is_pressed and tiempo_espera < 10 and not stop_event.is_set():
            STP.on()
            sleep(0.05)
            STP.off()
            sleep(0.05)
            tiempo_espera += 1

        if tiempo_espera >= 10:
            # Si no se activa el botón en 10 segundos, detener el motor
            print(f"Motor {k} se detuvo después de 10 segundos sin activar el botón.")
            motor_activo = False
            break

        # Si el botón se activa, el motor se detiene
        print(f"Motor {k} detenido. Esperando por posición deseada...")
        motor_activo = False
        sleep(0.1)  # Pausa para estabilizar

        # Espera hasta que se reciba la posición deseada
        print(f"Motor {k} activado, esperando posición...")
        motor_activo = True
        sleep(0.1)  # Pausa para evitar que se reinicie inmediatamente el ciclo sin esperar

    print(f"Hilo del motor {k} cerrado.")

def mover_motores(pasos):
    global motor1_activo, sentido1, motor2_activo, sentido2
    print("Ambos motores se moverán en sentido horario")

    # Mover motor 1
    DIR1.value = 1  # Sentido horario
    for _ in range(pasos):
        if not motor1_activo:
            break
        STP1.on()
        sleep(0.05)
        STP1.off()
        sleep(0.05)

    # Mover motor 2
    DIR2.value = 1  # Sentido horario
    for _ in range(pasos):
        if not motor2_activo:
            break
        STP2.on()
        sleep(0.05)
        STP2.off()
        sleep(0.05)

def obtener_distancia():
    while True:
        try:
            distancia = float(input("Ingrese la distancia en mm (positiva y menor a 200): "))
            if 0 < distancia < 200:
                return distancia
            else:
                print("Por favor, ingrese un valor válido.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

def calcular_pasos(distancia):
    pasos = int(distancia // STEP_DISTANCE)  # Redondear hacia abajo
    return pasos

def iniciar_control_motor(k):
    global motor1_thread, motor2_thread
    stop_event = motor1_stop_event if k == 1 else motor2_stop_event
    
    if k == 1:
        # Si el hilo de motor1 no está en ejecución, lo iniciamos
        if motor1_thread is None or not motor1_thread.is_alive():
            motor1_thread = threading.Thread(target=controlar_motor, args=(1,))
            motor1_thread.daemon = True
            motor1_thread.start()
    elif k == 2:
        # Si el hilo de motor2 no está en ejecución, lo iniciamos
        if motor2_thread is None or not motor2_thread.is_alive():
            motor2_thread = threading.Thread(target=controlar_motor, args=(2,))
            motor2_thread.daemon = True
            motor2_thread.start()

def detener_motor(k):
    stop_event = motor1_stop_event if k == 1 else motor2_stop_event
    stop_event.set()  # Activar la bandera de detención

try:
    while True:
        distancia = obtener_distancia()
        pasos = calcular_pasos(distancia)

        # Se reinicia el proceso de movimiento antihorario para ambos motores
        print(f"Recibida nueva posición: {distancia} mm.")
        
        # Activar los motores para que giren antihorario
        motor1_activo = True
        motor2_activo = True

        # Iniciar el ciclo de espera (botón o 10 segundos)
        iniciar_control_motor(1)
        iniciar_control_motor(2)

        # Después de 10 segundos o la activación de los botones, ambos motores se mueven la misma distancia en sentido horario
        mover_motores(pasos)

        # Detener los hilos después de mover los motores
        detener_motor(1)
        detener_motor(2)

except KeyboardInterrupt:
    print("\n  Deteniendo")
    # Detener los hilos si se interrumpe el programa
    detener_motor(1)
    detener_motor(2)
