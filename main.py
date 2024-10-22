# Algoritmo 7

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
          'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
          'Diciembre']

while True:
    month = int(input('Introduce el número del mes: '))
    if 0 <= month or month >= 12: print('No es un mes válido.')
    else: print(f'El mes {month} es {months[month - 1]}')


# Algoritmo 8 