Instrucciones en la pg. 312 del data sheet.

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
  - 1 Ciclo de bus: Operaciones aritméticas, lógicas, de movimiento
  - 2 Ciclos de bus: Mover registro a registro, salto incondicionales, saltos condicionales (cuando se produce un salto en una instrucción de 2 bytes)
  - 3 Ciclos de bus: Saltos condicionales (cuando se produce un salto en una instrucción de 4 bytes)


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

Registros de estado (status flags. pg. 73): Muestran el estado aritmético de la ALU. Dependen de la instrucción ejecutada
- N (Negative bit): 1 -> El resultado es negativo
- OV (Overflow bit): 1 -> Hay una sobrecarga en el resultado que sobrepasa los 7 bits
- Z (Zero bit): 1 -> El resultado es cero
- DC (Digit carry/borrow bit): 1 -> 
- C (Carry/borrow bit): 1 ->

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


Pasos para activar una interrupción:
1.) Borrar la bandera (IF - Interrupt Flag. Indicador de ocurrencia)
2.) Habilitar globalmente las interrupciones
3.) Habilitarla individualmente (IE - Interrupt Enable. Máscara)

Fuentes de reset:
- Power-on Reset (POR): Reset por corte de la fuente de alimentación
- Reset instruction: Instrucción de reset dentro del programa
- WatchDog Timer
- Master Clear
- Programmable Brown-out Reset (BOR): Reinicia el micro cuando el nivel de la batería baja hasta cierto valor (desabilitado por defecto).
- Stack Full Reset: Reset cuando se llena la pila (tiene 31 niveles de capacidad). Sucede en recursión.
- Stack Underflow: Cuando la pila se intenta vaciar cuando no hay nada

RCON indica cuál fuente de reset ocurrió. Contiene 4 bits. No hay bit de indicación para MCLR, se deduce por descarte.
STKPTR (Stack Pointer), indica el nivel de anidamiento --> Capacidad de la pila.


Modos de bajo consumo (Pg. 37):
- Modo de suspensión: Corta la señal de clk (CPU y periféricos)
- Modo de suspensión parcial (modo espera): Corta señal de clk (CPU) 


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
CONFIG FOSC=INTOSC_EC ;Internal Oscillator (External Clock) (1 MHz)
CONFIG FOSC=EC_EC ;External Oscillator
CONFIG FOSC=XT_XT ;Cristales con frecuencia menor a 4 MHz
CONFIG FOSC=HS ;Cristales con frecuencia 4 MHz - 40 MHz

// Configurar perro guardián. Por defecto está encendido
CONFIG WDT=OFF

// Configurar Master Clear (Reset externo)
CONFIG MCLRE=OFF

// Configuración en bajo voltaje
CONFIG LVP=OFF

// RB0 - RB4 comienzan siendo análogos. Para ajustarlos de modo digital se usa
CONFIG PBADEN=OFF

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

ORG 0h ; Se ejecuta cuando se resetea el micro
 goto Inicio ;Vector de reset
 
ORG 8h ;Se ejecuta cuando sucede una interrupción
 goto ISR ;Vector de interrupción

// Para configurar correctamente el perro guardián
CONFIG WDT=ON
bsf WDTCON,SWDTEN ;Enable WD
CONFIG WDPTS=<N> ;N: 1 - 32. Set WD time.

// Instrucciones. Presenta la estructura:
<Etiquetas> <Mnemónicos> <Operandos> <Comentarios>

// Las etiquetas identifican posiciones de memoria de las instrucciones
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

// Llamar a subrutinas (equivalente al llamado de funciones). Tabién modifica el contador del programa, pero guarda su posición actual. Tal posición
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

// Preguntar sobre una variable de estado
<Nmemónico condicional> STATUS, <Variable de estado>

// Modificar una variable de estado. Se recomienda solo usar BCF, BSF, SWAPF, MOVFF y MOVWF
<Nnemónico> STATUS, <Variable de estado>

cpfseq <Variable> ;Variable = W ?
cpfsgt <Variable> ;Variable > W ?
cpfslt <Variable> ;Variable < W ?

// Establecer el bit de un registro
bsf <registro>,<posición de bit del registro> ;Bit set file
bcf <registro>,<posición de bit del registro> ;Bit clear file

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




