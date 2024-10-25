
### DIAGRAMAS DE FLUJO

# 1. Algoritmo que pide tu nombre y lo imprime por pantalla

print('Tu nombre es {}'.format(input('Introduce tu nombre: ')))

# 2. Algoritmo que cuenta hasta el 10 e imprime por pantalla el número por el que va contando.

print('Esto es un contador:')
for n in range(0,10): print(n+1)

# 3. Algoritmo que simula mandar un mensaje de whatsapp

print('Abriendo la apliación de WhatsApp...')
contacto = input('Introduce el nombre del contacto al que le quieres mandar el mensaje: ')
print(f'Entrando al chat de {contacto}...')
mensaje = input('Introduce el mensaje que quieres enviar: ')
print('Enviando mensaje...')
print('Mensaje enviado.')

# 4. Algoritmo que escribe "Hola" cinco veces

for n in range(0,5): print('Hola')

# 5. Algoritmo que pide un número y calcula su raíz cuadrada

while True:
    numero = input('Introduce un número: ')
    if int(numero) < 0: print('No existe la raíz cuadrada de un número negativo')
    else: print(f'La raíz cuadrada de {numero} es {srqt(numero)}')


### PSEUDOCÓDIGO

# 1. Algoritmo que calcula el área de un triángulo

base = int(input('Introduce la base: '))
altura = int(input('Introduce la altura: '))
area = base * altura / 2
print(f'El área del triángulo es de {area}.')

# 2. Algoritmo en el que introduces tu nombre y tu edad y 
# muestra un mensaje de saludo

nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
print(f'Hola {nombre} encantado. Tienes {edad} años.')

# 3. Algoritmo que compara dos números y muestra cual 
# de ellos es mayor

n1 = int(input('Introduce el primer número: '))
n2 = int(input('Introduce el segundo número: '))

if n1 > n2 : 
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

print(f'El número mayor es {mayor} y el menor es {menor}')

# 4. Algoritmo que pide una cadena por teclado y luego se 
# visualiza en vertical

cadena = input('Introduce una cadena de caracteres: ')
print(f'La cadena tiene {len(cadena)} caracteres.')
for letra in cadena:
    print(letra)

# 5. Algoritmo que pide un número y muestra la tabla de 
# multiplicar de ese número

numero = int(input('Introduce un número: '))
print(f'La tabla de multiplicar del {numero} es:')
for n in range(0, 11):
    print(f'{n} x {numero} = {n*numero}')

# 6. Algoritmo para adivinar un número

from random import randint 

numero_aleatorio = random.randint(1,10)
while True:
    numero = int(input('Introduce un número entre el 1 y el 10'))
    if numero == numero_aleatorio:
        break
        else: print('Sigue intentandolo...')
print('Lo has adivinado. El número era: {}'.format(numero))

# 7. Algoritmo que pide el número de un mes y devuelve el mes en cuestión

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
        'Diciembre']

while True:
    month = int(input('Introduce el número del mes: '))
    if 0 <= month or month >= 12: print('No es un mes válido.')
    else: print(f'El mes {month} es {months[month - 1]}')

# 8. Algoritmo para determinar el precio de un producto en base a su cantidad 
# y su precio en relación con los kilogramos

products = {
    1 : {'name' : 'naranjas', 'price' : 1.90},
    2 : {'name' : 'mandarinas', 'price' : 3.35},
    3 : {'name' : 'limones', 'price' : 1.95},
    4 : {'name' : 'pomelos', 'price' : 2.85},
    5 : {'name' : 'kiwis', 'price' : 2.95},
    6 : {'name' : 'plátanos', 'price' : 3.55},
}
    
    
while True:

    for n in range(1,len(products)+1):
        print(f"{n}.- {products[n]['name'].capitalize()} ({products[n]['price']} €/kg)")
        
    n = int(input('\nIntroduzca el número de producto: '))

    if n <= 0 or n >= len(products): print('Número de producto no válido')
    else:
        kg = int(input('Introduzca el número de kg de producto: '))
        print(f"\nEl precio total es: {kg * products[n]['price']}€")
        break

# 9. Algoritmo anterior mejorado para que vuelva a presentar el menú y se puedan
# seguir preguntando precios.

import os

products = {
    1 : {'name' : 'naranjas', 'price' : 1.90},
    2 : {'name' : 'mandarinas', 'price' : 3.35},
    3 : {'name' : 'limones', 'price' : 1.95},
    4 : {'name' : 'pomelos', 'price' : 2.85},
    5 : {'name' : 'kiwis', 'price' : 2.95},
    6 : {'name' : 'plátanos', 'price' : 3.55},
}
    
while True:

    os.system('clear')

    for n in range(1,len(products)+1):
        print(f"{n}.- {products[n]['name'].capitalize()} ({products[n]['price']} €/kg)")
        
    n = int(input('\nIntroduzca el número de producto: '))

    if n <= 0 or n >= len(products): print('Número de producto no válido')
    else:
        kg = int(input('Introduzca el número de kg de producto: '))
        print(f"\nEl precio total es: {kg * products[n]['price']}€")
    input('Presione enter para continuar...')

# 10. Algoritmo que pida introducir una lista de números y los almacene en una dimensión, para ordenarlos posteriormente mediante el méotod de la burbuja

entrada = input('Introduce una lista de números separados por un espacio: ')
lista = [int(n) for n in entrada.split()]

for i in range(len(lista)):
    for j in range(0, len(lista)-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
    
print(f'Lista de números ordenados: {lista}')

# 11. Mismo algoritmo que el 8, pero pasando la visualización del menú a un subproceso.

def visualizacionMenu (products):
    for n in range(1,len(products)+1):
        print(f"{n}.- {products[n]['name'].capitalize()} ({products[n]['price']} €/kg)")

products = {
    1 : {'name' : 'naranjas', 'price' : 1.90},
    2 : {'name' : 'mandarinas', 'price' : 3.35},
    3 : {'name' : 'limones', 'price' : 1.95},
    4 : {'name' : 'pomelos', 'price' : 2.85},
    5 : {'name' : 'kiwis', 'price' : 2.95},
    6 : {'name' : 'plátanos', 'price' : 3.55},
}
    
while True:

    visualizacionMenu(products)
    n = int(input('\nIntroduzca el número de producto: '))

    if n <= 0 or n >= len(products): print('Número de producto no válido')
    else:
        kg = int(input('Introduzca el número de kg de producto: '))
        print(f"\nEl precio total es: {kg * products[n]['price']}€")
        break

# 12. Mismo algoritmo que el 10, pero pasando el método de ordenación de burbuja a un subproceso.

def metodoBurbuja (lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

entrada = input('Introduce una lista de números separados por un espacio: ')
lista = [int(n) for n in entrada.split()]
print(f'Lista de números ordenados: {metodoBurbuja(lista)}')

# 13. Algoritmo que simula a una calculadora

def suma (n1, n2): return n1 + n2
def resta (n1, n2): return n1 - n2
def multiplicacion (n1, n2): return n1 * n2
def division (n1, n2): return n1 / n2

menu = [
    '1.- Sumar',
    '2.- Restar',
    '3.- Multiplicar',
    '4.- Dividir\n'
]

for n in menu: print(n)
operacion = int(input('Escoja una opción: '))

n1 = int(input('Introduzca el primer valor: '))
n2 = int(input('Introduzca el segundo valor: '))

if operacion == 1: resultado = suma (n1, n2)
elif operacion == 2: resultado = resta (n1, n2)
elif operacion == 3: resultado = multiplicacion (n1, n2)
elif operacion == 4: resultado = division (n1, n2)

print(f'El resultado es: {resultado}')
