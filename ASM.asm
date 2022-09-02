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
  - 1 Ciclo de bus
  - 2 Ciclos de bus
  - 3 Ciclos de bus


El perro guardián es un tipo de protección ante códigos no deseados por el momento. Cuando el microcontrolador se encuentra en condiciones críticas, se reinicia.
Es un temporizador que corre desde cero, cuando llega hasta cierto límite (desborde), se reinicia el micro.

En la librería del micro C:\Program Files (x86)\Microchip\MPLABX\v3.30\mpasmx\p18f4550.inc se encuentran las direcciones de los registros

Para solucionar error de ensamblador relocalizador: Propiedades del proyecto -> mpasm (Global options) -> Build in absolute mode

Se puede llevar un seguimiento del registro W en el debugger con las variables al nombrar una  en la ventana como WREG
Se puede hacer lo mismo para los puertos

Visualizar pines: Window -> Simulator -> IO Pins

Generar un estímulo en la simulación de una señal digital: Window -> Simulator -> Stimulus

Los status flags en la parte superior del pantallazo de MPLabX, se muestra el estado de los registros de la memoria caché

Tras la sentencia end, se vuelve a repetir el código desde la primera instrucción. Se reinicia el micro de manera abrupta

Al debuggear podemos ir a la siguiente instrucción con F7

Fuentes de reloj del micro:
- Oscilador interno
- Oscilador externo
- Cristal

Los puertos del microcontrolador son: (X: A, B, C, D, E)
- TRISX
- LATX: Permite manipular salidas
- PORTX

Puerto B - Señales análogas
Puerto C - Comunicaciones y control
Puerto E - Funciones adicionales

Ajustar puertos como:
Entradas -> bsf <PUERTO>
Salidas -> clrf <PUERTO>




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
movlw <valor> ;Se crea la constante y se mueve al registro de trabajo w.
movwf <variable> ;Carga la constante presente en w a la variable.

// Es importante resaltar que 'mov' mueve un valor de un registro a otro. Entonces movwf mueve el valor desde w hasta f (representa la variable en el operando)

// Incrementar en 1 unidad una variable
incf <variable>

// Ir a una dirección del código
goto <etiqueta o dirección de memoria>

// Establecer el bit de un registro
bsf <registro>,<posición de bit del registro> ;Bit set file
bcf <registro>,<posición de bit del registro> ;Bit clear file

// Complemento a 1
comf <variable>

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

// Condición de salto (Bit Test File)
btfss <Puerto o variable>,<Bit del puerto> ;RXX = 1? Salta la siguiente línea de código cuando se cumple la condición
btfsc <Puerto o variable>,<Bit del puerto> ;RXX = 0? Salta la siguiente línea de código cuando se cumple la condición

// No hacer nada por un ciclo de bus
nop

// Incrementos y Decrementos
decf <Variable> ;Decrementa la variable
decfsz <Variable> ;Decrementa la variable. Salta 1 línea si la variable de entrada es 0.
decfsnz <Variable> ;Decrementa la variable. Salta 1 línea si la variable de entrada no es 0.

incf <Variable> ;Incrementa la variable
incfsz <Variable> ;Incrementa la variable. Salta 1 línea si la variable de entrada es 0.
incfsnz <Variable> ;Incrementa la variable. Salta 1 línea si la variable de entrada no es 0.

