"""
while True:
    print()
    num_1 = input("Digite um número: ")
    operador = input ("Digite um operador (+, -, /, *): ")
    num_2 = input("Digite um número: ")
    sair = input("Deseja sair? [s]im ou [n]ão: ")

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')         
"""
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
"""

acumulador_anterior = 0
contador = 0
acumulador = acumulador_anterior + contador

while contador <= 100:
    print(acumulador_anterior, contador, acumulador)
    
    contador += 1 
    acumulador_anterior = acumulador
    acumulador = acumulador_anterior + contador
    

   
     
