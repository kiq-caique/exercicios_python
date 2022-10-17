"""
faça um programa que peça ao usuário para digitar um número inteiro, informe se 
este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe
que não é um número inteiro.
"""
"""
numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)   
else:
    print('Valor inserido não é um numero inteiro')

if numero_inteiro % 2 == 0: 
    print(f'O numero digitado é par')    
else:
    print(f'O numero digitado é ímpar')     
"""

"""
Faça uma programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
 exiba a saudação apropriada. Ex: Bom dia 0-11; Boa tarde 12-17 e Boa noite 18-23.
"""
"""
horario = input ('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int (horario)
    
    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0-23')

    else:        
        if horario < 12:
            print('Bom dia!')

        if horario > 11 and horario < 18:
            print('Boa tarde!')

        if horario > 17:
            print('Bonasera katucha!')        
else:
    print("Por favor, digite um horário entre 0 e 23.")
"""    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva: "que nome curto!"; se tiver entre 5 e 6 letras, escreva: "Nome comum"
maior que 6 escreva "Seu nome é grande"
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Nome curto')
elif tamanho <= 6:
    print('Nome comum')    
else:
    print('Nome grande')