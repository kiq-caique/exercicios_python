""" pergunta1
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
""" resposta1
def func1():
    return 'Olá mundo!' 

def func2(x):
    return x()

executando = func2(func1)
print(executando)


"""

""" pergunta2
2 - Crie uma função1 que recebe uma função2 como parâmentro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um numero
diferente de arugmentos.
"""

def fun1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fun2(idade, nome):
    return f'{idade} anos nome: {nome}'

def fun12(nome, valor):
    return f'nome {nome} idade {valor}'

#funcao(*args, **kwargs): **kwargs recebe apenas argumentos com definições.ex:' nome= <'após o primeiro argumento "definido" todos os demais argumento posteriores deverão ser definidos tbm>
#fun2(idade, nome):
#fun2(30, 'carlos'):{30} anos nome: {carlos}
exec = fun1(fun2, 29, nome='carlos')
exec2 = fun1(fun12, nome='carlos' , valor=29) #eu posso tirar nome= e valor=, mas não posso tirar somente o nome= devido a definição de **kwargs
print(exec)
print(exec2)