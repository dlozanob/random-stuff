Instrucciones en la pg. 312 del data sheet.

Características del PIC18F4550:
- 8 bits
- Set de 77 instrucciones
- Memoria Flash de 32 kb
- 2 kb de memoria SRAM
- 256 B de memoria EEPROM
- 34 pines I/O y 13 pines análogos
- Puertos RS232, SPI, IIC, Paralelo y USB 2.0 Device
- 3 temporizadores de 16 bits y uno de 8 bits con dos canales de PWM
- 21 fuentes de interrupción
- 7 fuentes de reset
- Memoria RAM para datos de 4 kb
- Su voltaje de alimentación se encuentra en el rango: -0.3 - 7.5 V
- La corriente de entrada por el pin Vdd es de 250 mA
- 34 pines digitales

Registros de la memoria caché:
- Registro acumulador o de trabajo (W), 8 bits
- Registro de condiciones del programa (STATUS), 8 bits)
- Contador de programa (PC), 21 bits
- Apuntador de pila (SP), 5 bits
- Registros apuntadores (FSR0, FSR1, FSR2), 12 bits cada uno


Un programa se organiza en 4 secciones:
- Inclusión de librerías y definición de símbolos
- Directivas de configuración: Ajustan parámetros generales del funcionamiento del microcontrolador
- Definición de variables: No hay tipos de variables. Cada una tiene el tamaño de bits del micro.
- Instrucciones del ensamblador

El set de instrucciones RISC dota al microcontrolador de 75 instrucciones estándar y 8 del set extendido.

Tipos de instrucciones:
- Según su operación:
  - Operaciones orientadas a byte: Operaciones aritméticas, lógicas, o de movimiento a un registro o variable.
  - Operaciones orientadas a bit: Operan un solo bit de registro o variable.
  - Operación de control: Consultan o manipulan los registros de la CPU (a excepción del registro W).
  - Operación de constantes: Utilizan una constante para su ejecución.
  - Operaciones de manejo de tablas: Permiten la lectura o escritura de memorias FLASH.
  - Operación de set extendido: Añadidas para realizar funciones especiales.
  
- Según el modo de direccionamiento:
  - Inherente: No requieren operandos para su ejecución.
  - Inmediato: Operan con constantes en operaciones aritmético-lógicas.
  - Directo: Operan con un registro o variable que es especificado como operando.
  - Relativo: Saltan a un bloque del programa dependiendo del estado de una variable. (Saltan a posiciones de memoria cercanas)
    (Máximo salto: 128 posiciones hacia arriba, 127 posiciones hacia abajo)
  - Extendido: Saltan a cualquier posición de memoria. Funciona como el relativo.
  - Indirecto: Usan apuntadores para manipular registros y variables.
  
- Según el espacio que ocupan en memoria:
  MOVFF, CALL, GOTO, MOVSF, MOVSS ocupan 4 bytes. El resto de instrucciones ocupan 2 bytes.

- Según el tiempo que tardan en ejecutarse:
  - 1 Ciclo de bus: Instrucciones de 2 bytes. Operaciones aritméticas, lógicas, de movimiento
  - 2 Ciclos de bus: Instrucciones de 4 bytes. Mover registro a registro, salto incondicionales,
      saltos condicionales (cuando se produce un salto en una instrucción de 2 bytes)
  - 3 Ciclos de bus: Saltos condicionales (cuando se produce un salto en una instrucción de 4 bytes)


Apuntadores:
Apuntan a posiciones de la memoria RAM. Los registros e los apuntadores son FSR0, FSR1, FSR2.

Cada apuntador tiene 5 modos de acceso para el uso del modo indirecto:
- INDF: Se accede a la posición de memoria pero el apuntador no es modificado
- POSTINC: Se accede a la posición de memoria y posteriormente se incrementa la posición del apuntador
- POSTDEC: Se accede a la posición de memoria y posteriormente se decrementa la posición del apuntador
- PREINC: Antes de acceder a la posición de memoria, se incrementa la posición del apuntador
- PLUSW: La posición del contador se incrementa el valor que haya en el registro W


El perro guardián es un tipo de protección ante códigos no deseados por el momento. Cuando el microcontrolador se encuentra en condiciones críticas, se reinicia.
Es un temporizador que corre desde cero, cuando llega hasta cierto límite (desborde), se reinicia el micro (2 minutos por defecto). Funciona con un oscilador RC propio.

En la librería del micro C:\Program Files (x86)\Microchip\MPLABX\v3.30\mpasmx\p18f4550.inc se encuentran las direcciones de los registros

Para solucionar error de ensamblador relocalizador: Propiedades del proyecto -> mpasm (Global options) -> Build in absolute mode

Se puede llevar un seguimiento del registro W en el debugger con las variables al nombrar una en la ventana como WREG
Se puede hacer lo mismo para los puertos

Visualizar pines: Window -> Simulator -> IO Pins

Generar un estímulo en la simulación de una señal digital: Window -> Simulator -> Stimulus

Medir tiempos en las instrucciones: Window -> Debugging -> Stop watch

Tras la sentencia end, se vuelve a repetir el código desde la primera instrucción. Se reinicia el micro de manera abrupta

Al debuggear podemos ir a la siguiente instrucción con F7


Los status flags se encuentran en la parte superior del pantallazo de MPLabX


Registro STATUS (status flags. pg. 73): Muestran el estado aritmético de la ALU. Dependen de la instrucción ejecutada
- N (Negative bit): 1 -> El resultado es negativo
- OV (Overflow bit): 1 -> Hay una sobrecarga en el resultado que sobrepasa los 7 bits
- Z (Zero bit): 1 -> El resultado es cero
- DC (Digit carry/borrow bit): 1 -> Indica si se generó un acarreo de los 4 bits bajos a los 4 bits altos
- C (Carry/borrow bit): 1 -> Indica si se generó un acarreo total en los 8 bits


Fuentes de reloj del micro:
- Oscilador interno
- Oscilador externo
- Cristal

Los registros del microcontrolador son: (X: A, B, C, D, E)
- TRISX: Configura el estado I/O de los pines (1 -> Entrada)
- LATX: Permite manipular las salidas
- PORTX: Permite consultar el estado de las entradas

Puerto B - Señales análogas
Puerto C - Comunicaciones y control
Puerto E - Funciones adicionales

Ajustar puertos como:
Entradas -> bsf <PUERTO>
Salidas -> clrf <PUERTO>


EQU: Memoria de datos
ORG: Memoria de instrucciones


Interrupciones:

Cada interrupción tiene 3 bits para controlar su operación:
- IF (Interrupt Flag): Indicador de ocurrencia
- IE (Interrupt Enable): Máscara
- Priority bit: Seleccionar la prioridad de la interrupción

Se utilizan 10 registros para controlar la operación de interrupciones:
- RCON (Reset Control Register)
    Bits: IPEN (Interrupt Priority), SBOREN, RI, TO, PD, POR, BOR
- INTCON (Interrupt Control Register)
    Bits: GIE/GIEH (Global Interrupt), PEIE/GIEL, TMR0IE: IE de Timer0 cuando este llega a cierto límite de tiempo (overflow),
    INT0IE: IE de la interrupción externa 0, RBIE: IE de la interrupción de teclado, TMR0IF: IF de la interrupción (overflow) de Timer0,
    INT0IF: IF de la interrupción externa 0, RBIF: IF de la interrupción de teclado
- INTCON2: Contiene los bits de prioridad para Timer0 y la interrupción de teclado. Su bit RBPU permite habilitar resistencias de pull-up para
  todos los pines del puerto B (se recomienda poner un retardo después de habilitarla).
- INTCON3: Controla las interrupciones externas número 1y 2
- PIR1, PIR2
- PIE1, PIE2
- IPR1, IPR2

Pasos para activar una interrupción:
1.) Borrar la bandera (IF)
2.) Habilitarla individualmente (IE)
3.) Habilitar globalmente las interrupciones


Interrupción externa No. 0:

Solo funciona con el pin RB0 configurado como entrada
Su bit de habilitación es INT0IE
Su bit de indicación de ocurrencia es INT0IF

Se administra con el registro INTCON. Siempre es de alta prioridad. A las interrupciones externas INT1 e INT2 si se les puede ajustar la prioridad


Interrupción Timer0 (Pg. 127):

- Temporizador/contador de 8 o 16 bits
- Tiene un divisor de frecuencia (prescaler) de 1 hasta 256
- Su bit de habilitación es TMR0IE
- Su bit de indicación de ocurrencia es TMR0IF
- Su bit de configuración de prioridad es TMR0IP

Funciona como un contador (ej.: contar botellas en una banda) o un temporizador (reloj)
Su registro de control es T0CON (Timer0 Control Register):
  Bits: TMR0ON (habilita Timer0), T08BIT (ajusta Timer0 como un contador de 1 byte o 2),
  T0CS: Lo ajusta en modo temporizador o contador, T0SE: Indicar cambio en flancos de bajada o de subida, PSA, T0PS2, T0PS1,
  T0PS0 (TOPSx: Ajustan la escala de tiempo)


Interrupción de teclado: 

Se genera la interrupción por cualquier cambio producido en los pines RB4 - RB7. Ambos flancos disparan la interrupción.
Su bit de habilitación es RBIE
Su bit de indicación de ocurrencia es RBIF
Su bit de configuración de prioridad es RBIP
Los registros TMR0L (Timer0 Low) y TMR0H (Timer0 High) son registros que llevan la cuenta del conteo de Timer0 (son valores de precarga).
Timer0 parte baja (TMR0L) se usa como modo de conteo de 1 byte. Cuando tenemos el modo de conteo de 2 bytes, se usan ambos registros (ambos de 8 bits que suman 16 bits), se añade Timer0 parte alta para 
completar los 16 bits.


Fuentes de reset:
- Power-on Reset (POR): Reset por corte de la fuente de alimentación
- Reset instruction: Instrucción de reset dentro del programa
- WatchDog Timer
- Master Clear
- Programmable Brown-out Reset (BOR): Reinicia el micro cuando el nivel de la batería baja hasta cierto valor (desabilitado por defecto).
- Stack Full Reset: Reset cuando se llena la pila (tiene 31 niveles de capacidad). Sucede en recursión.
- Stack Underflow: Cuando la pila se intenta vaciar cuando no hay nada

RCON indica cuál fuente de reset ocurrió. Contiene 4 bits para este propósito (RI, TO, POR BOR).
No hay bit de indicación para MCLR, se deduce por descarte. (Pg. 46)
STKPTR (Stack Pointer), indica el nivel de anidamiento --> Capacidad de la pila. (Pg. 52)


Modos de bajo consumo (Pg. 37):
- Modo de suspensión: Corta la señal de clk (CPU y periféricos)
- Modo de suspensión parcial (modo espera): Corta señal de clk (CPU) 


Módulo RS232: Utiliza 3 registros de control

TXSTA:
- CSRC: No importa 
- TX9:
    1 -> Transmisión de 9 bits (noveno bit es de paridad)
    0 ->  Transmisión de 8 bits
- TXEN: Transmitir un bit enable
- SYNC: 
- SENDB: 
- BRGH:
- TRMT: Estado del registro (1-> Vacío)
- TX9D: Indicar qué bit se quiere transmitir como bit d información


RCSTA:
- SPEN: Encender el módulo de comunicación
- RX9: Configurar recepción de 9 u 8 bits (paridad)
- SREN: No importa
- CREN: Encender el receptor
- ADDEN: Auto detección de dirección (no importa)
- FERR: Error de marcado 
- OERR: Error de sobrescritura
- RX9D: 


BAUDCON
* Los bits 7 y 0: Opción de autodetección de velocidad (detecta la vel del otro dispositivo que intenta comunicarse con el PIC)
- ABDOVF: Indica si existe alguna operación de recepción
- RCIDL: Invertir la línea de recepción y transmisión
- RXDTP: Invertir dato de recepción
- TXCKP: Invertir dato de transmisión
- BRG16: Tiene que ver con la velocidad
- Unimplemented: - - -
- WUE (Wake-Up Enable Bit): Permite escoger qué hace el micro cuando está en bajo consumo
- ABDEN: 


Módulo de conversión Análogo a Digital:

Utiliza 5 registros:

- Result High Register (ADRESH): Parte alta de la conversión 
- Result Low Register (ADRESL): Parte baja de la conversión
- Control Register 0 (ADCON0)
    GO/DONE: Sirve para inciar la conversión. Al final de esta, indica que terminó la conversión.
    1 --> Está en coversión ; 0 --> Conversión finalizada
- Control Register 1 (ADCON1)
    VCFG0: Es la referencia baja de la conversión
    VCFG1: Es la referencia alta de la conversión
    PCFG3:PCFG0: Congfiguración de los pines como Análogo o Digital
- Control Register 2 (ADCON2)
    ADFM: Justificación a la derecha o a la izquierda
    ACQT2:ACQT0: Periodo de adquisición de la señal medida por el sensor
    ADCS2:ADCS0: Bits de selección del reloj de conversión


Módulo SPI:

El límite de esclavos son 28; ya que son 28 pines posibles a usar como salidas digitales en la configuración SPI


Módulo IIC:

Usa SDO, pero esto implica que perdemos el pin de recepción para el módulo RSD232
El módulo que permite la comunicación es MASTER SYNCHRONOUS SERIAL PORT (MSSP)

Usa dos registros: SPPSTAT, SPPCON1
Solo maneja 3 velocidades: 100 kb/s (estándar), 400 kb/s (alta),  3.4 mb/s (muy alta)

Pueden conectarse 127 esclavos distintos. Es posible conectar hasta 1023 esclavos.







----------------------------------------------------------------------------------------------------------------------------------------------------------



**********************************************************PRIMERA SECCIÓN - INCLUSIÓN DE LIBRERÍAS********************************************************

// Para incluir librerías se usa
include <nombre de la librería>.inc

// Incluimos la librería del microcontrolador
include P18F4550.inc


**********************************************************SEGUNDA SECCIÓN - DIRECTIVAS DE CONFIGURACIÓN***************************************************

// Las directivas de configuración adquieren la forma
CONFIG <parámetro a configurar>=<Estado>

// Configurar la frecuencia del oscilador
CONFIG FOSC = INTOSC_EC ;Internal Oscillator (External Clock) (1 MHz)
CONFIG FOSC = EC_EC ;External Oscillator
CONFIG FOSC = XT_XT ;Cristales con frecuencia menor a 4 MHz
CONFIG FOSC = HS ;Cristales con frecuencia 4 MHz - 40 MHz

// El pin RA6 tiene por defecto la función del módulo oscilador. Se puede desactivar con
CONFIG FOSC = INTOSC_ECIO 

// Configurar perro guardián. Por defecto está encendido
CONFIG WDT = OFF

// Configurar Master Clear (Reset externo). El pin RE3 tiene por defecto la función del módulo MCLR
Cuando este pin es liberado, solo se puede usar como entrada
CONFIG MCLRE = OFF

// Configuración en bajo voltaje. El pin RB5 tiene por defecto la función del módulo LVP
CONFIG LVP = OFF

// RB0 - RB4 comienzan siendo análogos porque tienen funciones del módulo ADC. Para ajustarlos a modo digital se usa
CONFIG PBADEN = OFF

// Los pines RC4 y RC5 tienen funciones del módulo USB. Se pueden desactivar haciendo '0' el tercer bit del registro UCON
Al hacer esto, los pines quedan como entradas digitales

// Hay 13 pines que tienen funciones del módulo ADC:
- RA0 - RA4
- RB0 - RB4
- RE0 - RE2
// Para liberar todos estos pines se escribe el valor de 15 en el registro ADCON1


****************************************************************TERCERA SECCIÓN - DEFINICIÓN DE VARIABLES*************************************************

// Definición de variables. La posición de memoria (dentro de la memoria RAM) está en el rango 000h - FFFh (h denota hexadecimal)
// El Access Bank es un banco de acceso rápido, el cual se compone de las primeras 96 posiciones
// Para PIC18, todas las variables tienen 8 bits
<nombre de la variable> equ <posición de memoria>

// Ejemplos de definición de variables
aux1 equ 1h
Var1 equ 9h
Var2 equ 1h
Var3 equ 0x7FF ;0x cuando usamos letras del sistema hexadecimal

// Asignar varias variables a una misma posición de memoria, hace que actúen de manera dinámica al funcionar como apuntadores
// Las variables son case-sensitive


********************************************************************CUARTA SECCIÓN - INSTRUCCIONES********************************************************

// Interrupciones
// Estructura de la declaración de una interrupción
ORG <Posición de memoria de la interrupción>
  .
  .

ORG 0h ; Se ejecuta cuando se resetea el micro
 goto Inicio ;Vector de reset
 
// Vector de alta prioridad en 8h, baja prioridad en 18h.
ORG 8h ;Se ejecuta cuando sucede una interrupción
 goto ISR ;Vector de interrupción

// La estructura de la ISR debe seguir
<Etiqueta de la ISR>
  .
  .
  retfie ;Retorna. Dura 2 ciclos de bus


// Para configurar correctamente el perro guardián
CONFIG WDT = ON
bsf WDTCON,SWDTEN ;Enable WD
CONFIG WDPTS = <N> ;N: 1 - 32. Set WD time.

// Instrucciones. Presenta la estructura:
<Etiquetas> <Mnemónicos> <Operandos> <Comentarios>

// Las etiquetas identifican posiciones de memoria de las instrucciones. Su sintaxis no puede contener espacios ni comenzar en números.
// Los mnemónicos son las abreviaturas que indican cada una de las instrucciones

// Ejemplo de la estructura de las instrucciones:
Inicio
  clrf TRISD ;Configuración de un registro
Menu
  setf aux1 ;Inicialización de una variable
  nop ;Retardo de un ciclo de bus
  bsf LATD,0 ;Manipulación de un único bit


// Comentarios
;<Comentario>

// Constantes: .<número>; ASCII: '<código ASCII>'; Hexadecimal: 0x<número>; Binario: b'<número de 8 bits>'; Octal: o'<número>'


// Sentencias

//IF
// Condicional sobre un bit. En caso de RC0=1, se salta la línea goto. Si la condición no se cumple, no se salta la línea.
// btfss --> Pregunta si el bit es 1; btfsc --> Pregunta si el bit es 0
MENU
  ***********************************
  btfss PORTC,0 ;RC0==1?
  goto SIGUIENTE
  nop
  ***********************************
SIGUIENTE 

// Condicional sobre una variable
MENU
  ***********************************
  tstfsz var1 ;var1==0?
  goto SIGUIENTE
  nop
  ***********************************
SIGUIENTE 

// Condicional sobre la comparación de variables
MENU
  ***********************************
  movf var1,w ;Cargamos la variable al registro W
  cpfseq var2 ;var1==var2?
  goto Siguiente
  nop
  ***********************************
SIGUIENTE

MENU
  ***********************************
  movf var1,w ;Cargamos la variable al registro W
  cpfsgt var2 ;var1>var2?
  goto Siguiente
  nop
  ***********************************
SIGUIENTE 

MENU
  ***********************************
  movf var1,w ;Cargamos la variable al registro W
  cpfslt var2 ;var1<var2?
  goto Siguiente
  nop
  ***********************************
SIGUIENTE 

// Condicional sobre los acarreos
// bc hace un salto relativo
MENU
  ***********************************
  movf var1,w ;Cargamos la variable al registro W
  addwf var2,w ;Se suma var2 con la variable presente en W (var1). El resultado se guarda en W.
  bc HayAcarreo ;C==1?
  ***********************************
HayAcarreo

// Condicional con sentencia ELSE

Menu
  ***********************************
  btfss PORTC,0 ;RC0==1?
  goto Apagar
  goto Encender
Encender
  ***********************************
    goto Siguiente
Apagar    
  ***********************************  
Siguiente 

// SWITCH
// opc será nuestra variable de control con la cual comparamos todos los casos
Sentencia_SWITCH
  movlw A
  cpfseq opc ;opc==A?
  goto PreguntarB
  goto CasoA
PreguntarB
  movlw B
  cpfseq opc ;opc==B?
  goto PreguntarC
  goto CasoB
PreguntarC

// WHILE o REPEAT
CicloWhile
  btfss PORTB,0 ;RB0==1?
  goto FinCiclo
  ***********************
  goto CicloWhile
FinCiclo
  ***********************

// FOR
// contador es nuestra variable de control
InicioCicloFor
  clrf contador
CicloFor
  movlw .5 ;Cargamos al registro W un tope igual a 5
  cpfslt contador ;contador<5?
  goto FinCiclo
  ***********************
  incf contador,f ;Incrementamos el contador en 1 y lo sobreescribimos
  goto CicloFor
FinCiclo
  ***********************
 
// Asignar pines a un puerto
  movlw b'11001100'
  movwf TRISE ; Se asignan los 8 pines al puerto TRISE
 
 
 
 // Terminar el código
end
  



---------------------------------------------------------------------------------------------------------------------------------------------------------- 
 
 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////////// MNEMÓNICOS ///////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

// Asignación binaria de una variable
clrf <registro o variable> ;Limpia un registro o variable. Asigna 0.
setf <registro o variable> ;Limpia un registro o variable. Asigna 1.

// Inicializar una variable
movlw <valor> ;Se crea la constante y se mueve al registro de trabajo W.
movwf <variable> ;Carga la constante presente en W a la variable.
movf <variable>, w ;Mover variable al registro W.

// Es importante resaltar que 'mov' mueve un valor de un registro a otro. Entonces movwf mueve el valor desde w hasta f (representa la variable en el operando)

// Incrementar en 1 unidad una variable
incf <variable>

// Saltos incondicionales: goto, call
// Ir a una dirección del código. Modifica el contador del programa
goto <etiqueta o dirección de memoria>

// Llamar a subrutinas (equivalente al llamado de funciones). También modifica el contador del programa, pero guarda su posición actual. Tal posición
se guarda en la pila del micro. Call introduce valores en la pila, return los saca. Se pueden guardar valores en la pila hasta 31 veces, luego el
micro se reinicia. El micro puede reiniciarse también si al sacar un valor de la pila no hay nada.
call <Etiqueta> ;Llama a la etiqueta
.
.
<Etiqueta>
return ;Retorna a la línea inmediatamente después de call

// Saltos condicionales: Tienen la letra 's' (skip)
// Condición de salto binaria (Bit Test File)
btfss <Puerto o variable>,<Bit del puerto> ;RXX = 1? Salta la siguiente línea de código cuando se cumple la condición
btfsc <Puerto o variable>,<Bit del puerto> ;RXX = 0? Salta la siguiente línea de código cuando se cumple la condición

cpfseq <Variable> ;Variable = W ?
cpfsgt <Variable> ;Variable > W ?
cpfslt <Variable> ;Variable < W ?

// Preguntar sobre una variable de estado
<Nmemónico condicional> STATUS, <Variable de estado>

// Modificar una variable de estado. Se recomienda solo usar BCF, BSF, SWAPF, MOVFF y MOVWF
<Nnemónico> STATUS, <Variable de estado>

// Establecer el bit de un registro
bsf <registro>,<posición de bit del registro> ;Bit set file
bcf <registro>,<posición de bit del registro> ;Bit clear file
btg <registro>,<posición de bit de registrp> ;Bit toggle

// Complemento a 1
comf <variable>

// Complemento a 2
negf <variable>

// Algunos operandos producen un resultado que se puede guardar en un lugar específico, siguen la forma:
<operando> <variable>,<d> ;Si d = 0, el resultado se guarda en W. Si d = 1, el resultado se guarda en la misma variable.

// Sumar
addwf <variable> ;W <- W + variable
addlw <Constante> ;W <- W + constante

// Restar (Flags: Z = 1 si 0. C = 0 si negativo)
sublw <Constante> ;l - w
subwf <Variable> ;f - w

// Bitwise operators
andwf <Variable> ;Variable & W
iorwf <Variable> ;Variable | W
xorwf <Variable> ;Variable xor W
andlw <Constante> ;Constante and W
iorlw <Constante> ;Constante or W
xorlw <Constante> ;Constante xor W

// Para generar saltos computados se puede modificar el registro PCL que corresponde al registro del contador del programa (PC)

// Los registros de los apuntadores de la memoria RAM son FSR0, FSR1, FSR2
Ejemplo de apuntadores:
Tabla equ 6h
*************
Menu  
  lfsr 0, Tabla ; Guarda en FSR0 el valor correspondiente a la dirección 0x6 en la memoria RAM

// Llenar una tabla en la memoria RAM con apuntadores
Ejemplo:
LlenarTabla
  lfsr 0, Tabla ; Se asigna al apuntador FSR0 la posición de memoria
  movlw 'H' ; Se carga una constante al registro W
  movwf POSTINC0 ; Se carga la constante al apuntador y se incrementa su posición
  movwf 'o'
  movwf POSTINC0 ; Se carga la constante al apuntador y se incrementa su posición
  .
  .
  return
  
Ejemplo:
LeerTabla
  lsfr 0, Tabla ; Se inicializa el apuntador con la primera posición de la tabla
  movf PLUSW0,w ; Se le suma un cierto valor al apuntador, y el valor donde está apuntando se guarda en W
  return


// No hacer nada por un ciclo de bus
nop

// Incrementos y Decrementos
decf <Variable> ;Decrementa la variable
decfsz <Variable> ;Decrementa la variable. Salta 1 línea si la variable de entrada es 0.
decfsnz <Variable> ;Decrementa la variable. Salta 1 línea si la variable de entrada no es 0.

incf <Variable> ;Incrementa la variable
incfsz <Variable> ;Incrementa la variable. Salta 1 línea si la variable de entrada es 0.
incfsnz <Variable> ;Incrementa la variable. Salta 1 línea si la variable de entrada no es 0.

// Salir de una ISR
retfie

// Reiniciar el micro de manera segura
reset

// Borrar cuenta del perro guardián
clrwdt ;Se reinicia su temporizador

// Modos de bajo consumo
bsf OSCCON, IDLEN ;Registro OSCCON (0 por defecto): 1 --> Modo de bajo consumo parcial; 0 --> Modo de bajo consumo total.
sleep ;Entra en modo de bajo consumo




