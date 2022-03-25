import os
import random
import dados_ascii 


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


print('''
                      +-----------------------------------------+
                      |       SIMULADOR DE TIRADA DE DADOS      |
                      +-----------------------------------------+
''')
ENTER = input('Presione ENTER para tirar el dado.')
clearConsole()

seguir = 'S'
while seguir == 'S':
    numero = random.randint(1, 6)
    print(str(numero).rjust(29))
    print(dados_ascii.dados_ascii[numero])

    # Bucle para comprobar que el usuario ingrese 's, n, S o N.
    while True:  
        seguir = input('\n¿Quiere tirar el dado nuevamente? [S/N] ')
        if not seguir.isalpha():
            print('\nError: has ingresado un caracter incorrecto.')
        elif seguir.upper() == 'S' or seguir.upper() == 'N':
            break
        else:
            print('\nError: has ingresado una letra incorrecta.')

    seguir = seguir.upper()
    clearConsole()