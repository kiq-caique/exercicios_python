""" pergunta_1
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao
 e nome.
"""
""" resposta_1
def saudacao(saudacao, nome):
    print(f'{saudacao}, {nome}')

saudacao('Olá', 'Carlos')
saudacao('Hey', 'Nilo')
saudacao('Eai', 'Jp')
"""

""" pergunta_2
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
""" resposta_2
def soma(n1, n2, n3):
     print(n1 + n2 + n3)

soma (1, 3, 5)
soma (4, 5, 6)
soma (3, 2, 1)   
"""

""" pergunta_3
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um 
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
""" resposta_3

def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumento_percentual (50, 60)
print(ap)
ap = aumento_percentual(100, 210)
print(ap)
"""

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

from tkinter.font import names


n = int(input(' Digite um valor '))

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n

print (fb(n))

# from random import randint

# for i in range(100):
#     aleatorio = randint(0, 100)
#     print(fb(aleatorio))