import os
import random
import dados_ascii 


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


print('''
      +-----------------------------------------+
      |      SIMULADOR DE TIRADA DE DADOS       |
      +-----------------------------------------+
''')
ENTER = input('Presione ENTER para tirar el dado.')
clearConsole()

seguir = 'S'
while seguir == 'S':
    numero = random.randint(1, 6)
    print(str(numero).rjust(23))
    print(dados_ascii.dados_ascii[numero])

    while True:  
        seguir = input('\n¿Quiere tirar el dado nuevamente? [S/N] ').upper()
        if seguir == 'S' or seguir == 'N':
            break
        else:
            print('\nERROR: ha ingresado un carácter invalido.')      
    clearConsole()