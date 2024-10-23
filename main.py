# Algortimo que calcula el área

def algoritmo1 ():
    base = int(input('Introduce la base: '))
    altura = int(input('Introduce la altura: '))
    area = base * altura / 2
    print(f'El área del triángulo es de {area}.')

# Algoritmo en el que introduces tu nombre y tu edad y muestra
# un mensaje de saludo

def algoritmo2 ():
    nombre = input('Introduce tu nombre: ')
    edad = input('Introduce tu edad: ')
    print(f'Hola {nombre} encantado. Tienes {edad} años.')

# Algoritmo que compara dos números y muestra cual de ellos
# es mayor

def algoritmo3 ():
    n1 = int(input('Introduce el primer número: '))
    n2 = int(input('Introduce el segundo número: '))

    if n1 > n2 : 
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

    print(f'El número mayor es {mayor} y el menor es {menor}')

# Algoritmo que pide una cadena por teclado y luego
# se visualiza en vertical

def algoritmo4 ():
    cadena = input('Introduce una cadena de caracteres: ')
    print(f'La cadena tiene {len(cadena)} caracteres.')
    for letra in cadena:
        print(letra)

# Algoritmo que pide un número y muestra la tabla
# de multiplicar de ese número

def algoritmo5 ():
    numero = int(input('Introduce un número: '))
    print(f'La tabla de multiplicar del {numero} es:')
    for n in range(0, 11):
        print(f'{n} x {numero} = {n*numero}')

# Algoritmo para adivinar un número

from random import randint 

def algoritmo6 ():
    numero_aleatorio = random.randint(1,10)
    while True:
        numero = int(input('Introduce un número entre el 1 y el 10'))
        if numero == numero_aleatorio:
            break
        else: print('Sigue intentandolo...')
    print('Lo has adivinado. El número era: {}'.format(numero))

# Algoritmo 7

def algoritmo7():

    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
            'Diciembre']

    while True:
        month = int(input('Introduce el número del mes: '))
        if 0 <= month or month >= 12: print('No es un mes válido.')
        else: print(f'El mes {month} es {months[month - 1]}')

# Algoritmo 8

def algoritmo8():

    products = {
        1 : {'name' : 'naranjas', 'price' : '1,90'},
        2 : {'name' : 'mandarinas', 'price' : '3,35'},
        3 : {'name' : 'limones', 'price' : '1,95'},
        4 : {'name' : 'pomelos', 'price' : '2,85'},
        5 : {'name' : 'kiwis', 'price' : '2,95'},
        6 : {'name' : 'plátanos', 'price' : '3,55'},
    }
    
    while True:

        for n in range(0,len(products)):
            print(f'{n+1}.- {products[n]['name']} ({products[n][price]} €/kg)')
        
        n = int(input('Introduzca el número de producto: '))

        if n <= 0 or n >= len(products): print('Número de producto no válido')
        else:
            kg = int(input('Introduzca el número de kg de producto: '))
            print(f'El precio total es: {kg * products[n-1][int(price)]}')
            break
