from gpiozero import OutputDevice, Button
import time
import threading


class Actuator_Interface:
    def __init__(self, top=None):
        self.DIR1 = 17
        self.STP1 = 27
        self.BTN1 = 5
        self.DIR2 = 23
        self.STP2 = 24
        self.BTN2 = 6

        self.motor1_activo = True
        self.sentido1 = True
        self.motor2_activo = True
        self.sentido2 = True

        self.PULLEY_DIAMETER = 18  # mm
        self.STEPS_PER_REV = 6400
        self.CIRCUMFERENCE = 3.1416 * self.PULLEY_DIAMETER
        self.STEP_DISTANCE = self.CIRCUMFERENCE / self.STEPS_PER_REV  # mm por paso

        # Crear objetos de gpiozero para los pines
        self.dir1 = OutputDevice(self.DIR1)
        self.stp1 = OutputDevice(self.STP1)
        self.btn1 = Button(self.BTN1)
        self.dir2 = OutputDevice(self.DIR2)
        self.stp2 = OutputDevice(self.STP2)
        self.btn2 = Button(self.BTN2)

        button1_thread = threading.Thread(target=self.controlar_motor1)
        button1_thread.daemon = True
        button1_thread.start()

        button2_thread = threading.Thread(target=self.controlar_motor2)
        button2_thread.daemon = True
        button2_thread.start()

        distancia = self.obtener_distancia(5)
        pasos = self.calcular_pasos(distancia)    
        motor1_thread = threading.Thread(target=self.mover_motor1, args=(pasos,))
        motor2_thread = threading.Thread(target=self.mover_motor2, args=(pasos,))
        motor1_thread.start()
        motor2_thread.start()
        motor1_thread.join()
        motor2_thread.join()    
        print("Motors Initialized")

    def controlar_motor1(self):
        global motor1_activo, sentido1
        while True:
            if self.btn1.is_pressed:
                print("pressed BTN1")
                motor1_activo = False
                sentido1 = not sentido1
                time.sleep(0.5)
            else:
                motor1_activo = True
                time.sleep(0.5)
            time.sleep(0.1)

    def mover_motor1(self, pasos):
        global motor1_activo, sentido1
        print("running motor1")
        self.dir1.value = 1 if sentido1 else 0
        for _ in range(pasos):
            if not motor1_activo:
                break
            self.stp1.on()
            time.sleep(0.05)
            self.stp1.off()
            time.sleep(0.05)

    def controlar_motor2(self):
        global motor2_activo, sentido2
        while True:
            if self.btn2.is_pressed:
                print("pressed BTN2")
                motor2_activo = False
                sentido2 = not sentido2
                time.sleep(0.5)
            else:
                motor2_activo = True
                time.sleep(0.5)
            time.sleep(0.1)

    def mover_motor2(self, pasos):
        global motor2_activo, sentido2
        print("running motor2")
        self.dir2.value = 1 if sentido2 else 0
        for _ in range(pasos):
            if not motor2_activo:
                break
            self.stp2.on()
            time.sleep(0.05)
            self.stp2.off()
            time.sleep(0.05)

    def obtener_distancia(self, dist):
        while True:
            try:
                #distancia = float(input("Ingrese la distancia en mm (positiva y menor a 200): "))
                distancia = float(dist)
                if 0 < distancia < 200:
                    return distancia
                else:
                    print("Por favor, ingrese un valor válido.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")

    def calcular_pasos(self, distancia):
        pasos = int(distancia // self.STEP_DISTANCE)  # Redondear hacia abajo
        return pasos


# try:
#     while True:
#         distancia = obtener_distancia(5)
#         pasos = calcular_pasos(distancia)
#         motor1_thread = threading.Thread(target=mover_motor1, args=(pasos,))
#         motor2_thread = threading.Thread(target=mover_motor2, args=(pasos,))
#         motor1_thread.start()
#         motor2_thread.start()
#         motor1_thread.join()
#         motor2_thread.join()
# except KeyboardInterrupt:
#     print("\n  Deteniendo")
