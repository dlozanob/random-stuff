Microchip presenta su propio compilador xc8. El compilador transforma desde lenguaje C a ensamblador.
MPASMWIN transforma desde ensamblador a binario.
Las variables enteras son de 16 bits.
Permite crear varios archivos en un mismo proyecto a diferencia de Assembler.
  
Se pueden escribir instrucciones en Assembly en C, siempre y cuando no afecten los registros de la memoria caché: NOP, RESET, SLEEP
  
----------------------------------------------------------------------------------------------------------------------------------------------------------
  
  
**********************************************************PRIMERA SECCIÓN - INCLUSIÓN DE LIBRERÍAS********************************************************

// Para incluir librerías se usa
#include <<librería>.h>

// La librería a usar es
#include <xc.h>

// Librería del LCD
#include "LibLCDXC8.h"

// Otras librerías útiles
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Al utilizar '<>' en el nombre de la librería, MPLabX busca en las carpetas de las librerías por defecto. Poner '" "' especifica que la librería se
// encuentra en la misma carpeta del proyecto (librerías personales).

// Decirle al compilador la frecuencia de reloj
#define _XTAL_FREQ <Frecuencia en Hz>









**********************************************************SEGUNDA SECCIÓN - DIRECTIVAS DE CONFIGURACIÓN***************************************************


// Presentan la estrictura
#pragma config <Configuración>

// Configuración de reloj
#pragma config FOSC=INTOSC_EC

// Configurar perro guardián
#pragma config WDT=OFF



  
****************************************************************TERCERA SECCIÓN - DEFINICIÓN DE VARIABLES*************************************************
  
// Caracteres (8 bits)
char a;

// Enteros (16 bits)
int b;

// Long (32 bits)
long c;

// Punto flotante (24 bits)
float d;

// Double (24 bits)
double e;

// Apuntadores (su tamaño es el mismo de la memoria del micro)
<Tipo de variable> *<Nombre>;

// Utilizar todos los bits de una variable
unsigned char a; //En este caso usa los 8 bits de la variable a

// Utilizar todos los bits con valores negativos  (-128 - 127)
signed char a;

// Arreglos
char f[3]={1,2,0};

// Matrices
int g[3][3];

// Se puede hacer una variable de 64 bits con:+
long long a;



********************************************************************CUARTA SECCIÓN - INSTRUCCIONES********************************************************
  
// Declarar la función principal
void main(void) {
    
}  
  
// Binario: '0b' ; Hexadecimal: '0x' ; ASCII: 'A'

// Asignar puertos
TRIS<Grupo de puerto> = <valor>
  
// Asignar un solo pín
TRIS<Grupo de puerto><# de pin> = <valor>;
TRISD0 = 0;
 
// Asignar varios pines a un registro
TRIS<Grupo de puerto> = 0b<Valor de los pines>
TRISB = 0b10100011

// Modificar puertos
 LATD0 = 0;
  
// Ciclos While
while(<condición>) {
}

// Es válido
while(TRMT == 0);


// Retardos
__delay_ms(<Tiempo en milisegundos>);
__delay_us(<Tiempo en microsegundos>);


// Interrupciones (ejemplo instruccón externa 0)
INT0IE = 1; // Habilitar interrupción
INT0IF = 0; // Borrar la bandera
GIE = 1; // Habilitar globalmente las interrupciones

// Para establecer los valores de precarga TMR0H y TMR0L
TMRO = <Valor de precarga>;

// Se debe declarar la función antes de Main (esqueleto)
void interrupt ISR(void);
  
// Definir la función de la interrupción
void interrupt ISR(void) {
    INT0IF = 0;
    NOP();
}

// Para baja prioridad
void __interrupt ISR(low_priority);
  
// Modificar uno de los bits de un registro
// Ejemplo:
RCONbits.IPEN = 1;
  
// Entrar en modo de bajo consumo total
sleep();
  
  
  
  192.168.1
    192.168.1.254
  
  
  
  
  
  
  
  
  
  
  
