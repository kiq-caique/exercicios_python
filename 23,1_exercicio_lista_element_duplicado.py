"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

"""PASSO A PASSO EXERCICIO AULA 23

1º A primeira coisa que eu vou começar a fazer é começar a fazer um *for* 
 nessa lista e pegar todas as listas """

# for lista in lista_de_listas_de_inteiros:
#     print(lista)
     
     #OBTENDO O RESULTADO COMENTADO A BAIXO.

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    # [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    # [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    # [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    # [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    # [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    # [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    # [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    # [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    # [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

"""
2º #1 Então agora que eu já sei que eu já tenho essa lista agora eu vou 
começar a fazer a minha função então *def* chamando de primeiro_duplicado
e essa lista ela vai receber uma lista *verific_lista*. #2 Depois vou simplesmente
retornar essa *verific_lista* e vou passar a minha *primeiro_duplicado* dentro
da minha função: print(primeiro_duplicado(lista)) passando a lista que estava
no *for* para dentro da função"""


# def primeiro_duplicado(verific_lista): #1
#         return verific_lista  #1

# for lista in lista_de_listas_de_inteiros: #2
#     print(primeiro_duplicado(lista)) #2

"""
3º #1 Agora irei pegar os elementos verificados 
jogando dentro de um *set* vazio, #2 e fazer um *for*
na lista que estou recebendo e vou jogar os meus numeros
dentro do *set*. Então se você observar #3 aqui a cada número 
que eu passar aqui dentro da minha lista eu vou jogar dentro
Esse número que eu estou checando na verdade são 
cada um dos números da lista interna. #4 Agora antes irei adicionar
um *if* para checar se o elemento 'numero' dentro da *verific_lista*
está dentro dos meus 'numeros_checados' caso o 'numero' q for averiguado
pelo programa, ja estiver dentro do 'numeros_checados', ele será meu
primeiro duplicado. 5# Então o que eu vou fazer 'primeiro_duplicado' = -1
porque eu tenho que retornar -1 conforme enunciado. 6# então eu troco o
*return verific_lista* por *return primeiro_duplicado* Então se eu não 
encontrar nada e se eu não fizer nada nesse *for* eu vou retornar '-1'
#7 caso o numero a ser averiguado pelo programa ja estiver dentro do meu
*set()* eu adiciono abaixo do if a condição de primeiro_duplicado = numero
#8 daí se eu encontrei já o meu primeiro duplicado não faz sentido continuar 
esse *for* porque eu já encontrei meu primeiro duplicado então vou dar um
break. #9 Agora para fazer uma verificação para saber se está correto, eu 
acrescento no print(primeiro_duplicado(lista)) a 'verific_lista'
ficando assim : print(lista, primeiro_duplicado(lista))
"""
def primeiro_duplicado(verific_lista): 
        numeros_checados = set() #1
        primeiro_duplicado = -1 #5

        for numero in verific_lista: #2
            if numero in numeros_checados: #4
                primeiro_duplicado = numero #7
                break    #8

            numeros_checados.add(numero) #3 

        return primeiro_duplicado #6  

for lista in lista_de_listas_de_inteiros:
    print(lista, primeiro_duplicado(lista)) #9