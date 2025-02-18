from gpiozero import LED, Button
from time import sleep
import threading


class Actuator_Control:
    def __init__(self):
        # Definición de pines
        self.DIR1 = LED(23)
        self.STP1 = LED(24)
        self.BTN1 = Button(5)
        self.DIR2 = LED(17)
        self.STP2 = LED(27)
        self.BTN2 = Button(6)

        self.BTN = self.BTN1
        self.DIR = self.DIR1
        self.STP = self.STP1

        # Variables de control
        self.motor1_activo = False
        self.motor2_activo = False

        self.motor_activo = self.motor1_activo

        self.sentido1 = True  # Sentido antihorario
        self.sentido2 = True  # Sentido antihorario

        # Características físicas del motor
        self.PULLEY_DIAMETER = 18  # mm
        self.STEPS_PER_REV = 3200
        self.CIRCUMFERENCE = 3.1416 * self.PULLEY_DIAMETER
        self.STEP_DISTANCE = self.CIRCUMFERENCE / self.STEPS_PER_REV  # mm por paso

        # Hilos de control de los motores
        self.motor1_thread = None
        self.motor2_thread = None

        # Eventos de detención para los hilos
        self.motor1_stop_event = threading.Event()
        self.motor2_stop_event = threading.Event()

        self.stop_event = self.motor1_stop_event

        self.iniciar_control_motor(1)
        self.iniciar_control_motor(2)


    def controlar_motor(self, k):
        self.motor_activo = self.motor1_activo 
        if k == 1:
            self.motor_activo = self.motor1_activo 
            self.BTN = self.BTN1 
            self.STP = self.STP1
            self.stop_event = self.motor1_stop_event
        elif k == 2:
            self.motor_activo = self.motor2_activo
            self.BTN = self.BTN2 
            self.STP = self.STP2
            self.stop_event = self.motor2_stop_event

        while not self.stop_event.is_set():  # El hilo continuará hasta que se active la bandera de detención
            print(f"Motor {k} moviéndose en sentido antihorario hasta que se active el botón")

            tiempo_espera = 0
            while not self.BTN.is_pressed and tiempo_espera < 5000 and not self.stop_event.is_set():
                print('posicionando en 0')
                self.STP.on()
                sleep(0.0001)
                self.STP.off()
                sleep(0.0001)
                tiempo_espera += 1

            if tiempo_espera >= 5:
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

    def set_dir(self, dir):
        if dir:
            self.DIR1.on()
            self.DIR2.on()
        else:
            self.DIR1.off()
            self.DIR2.off()

    def mover_motores(self, pasos, k):
        print("Ambos motores se moverán en sentido horario")
        self.STP = self.STP1 if k == 1 else self.STP2
        self.motor_activo = self.motor1_activo if k == 1 else self.motor2_activo
        # Mover motor k
        for _ in range(pasos):
            if not self.motor_activo:
                break
            print('posicionando')
            self.STP.on()
            sleep(0.0001)
            self.STP.off()
            sleep(0.0001)


    def obtener_distancia(self):
        while True:
            try:
                distancia = float(input("Ingrese la distancia en mm (positiva y menor a 200): "))
                if 0 < distancia < 200:
                    return distancia
                else:
                    print("Por favor, ingrese un valor válido.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")

    def calcular_pasos(self, distancia):
        pasos = int(distancia // self.STEP_DISTANCE)  # Redondear hacia abajo
        return pasos

    def iniciar_control_motor(self, k):
        stop_event = self.motor1_stop_event if k == 1 else self.motor2_stop_event
        
        if k == 1:
            # Si el hilo de motor1 no está en ejecución, lo iniciamos
            if self.motor1_thread is None or not self.motor1_thread.is_alive():
                self.motor1_thread = threading.Thread(target=self.controlar_motor, args=(0,))
                self.motor1_thread.daemon = True
                self.motor1_thread.start()
        elif k == 2:
            # Si el hilo de motor2 no está en ejecución, lo iniciamos
            if self.motor2_thread is None or not self.motor2_thread.is_alive():
                self.motor2_thread = threading.Thread(target=self.controlar_motor, args=(0,))
                self.motor2_thread.daemon = True
                self.motor2_thread.start()

    def detener_motor(self, k):
        stop_event = self.motor1_stop_event if k == 1 else self.motor2_stop_event
        stop_event.set()  # Activar la bandera de detención