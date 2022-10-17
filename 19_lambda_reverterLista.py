# def func(arg, arg2):
#     return arg * arg2

# var = func(2,3)
# print(var)
""" usando lambda para escrever a mesa função acima"""

# a = lambda x, y: x * y

# print(a(2,3))

lista = [
    ['P1', 13],
    ['P2', 5],
    ['P3', 25],
    ['P4', 19],
    ['P5', 50],
]

def func(item):
    return item[1]

lista.sort(key=func, reverse = True) #em caso de ordem decrescente, use *reverse*
print(lista)

"""Lambda é um função anônima (iremos aprender mais no decorrer do curso) mas a
função acima poderá ser escrita da seguinte maneira abaixo. obs: item pode ser 
qualquer nome, ele apenas irá refenciar os elementos dentro da lista e entre as
chaves será colocado o índice dos itens da lista ao qual deseja utilizar."""

# lista.sort(key=lambda item: item[1], reverse = True) #mais uma vez está na forma descrescente.
# print(lista)

"""Outro modo de escrever a função acima é com *sorted* (o elemento item acima mudei 
para i sem necessidade, apenas para mostrar q pode ser qlqr coisa."""

# print(sorted(lista, key=lambda i: i[1], reverse=False))#False OR True SEMPRE MAIUSCULA


"""RESUMÃO: A função *sorted* coloca as coisas em ordem. a função lambda substitui
a definição de uma função *def* e nao precisa do parênteses para passar os argumentos
posso passar qntos agurmentos desejar separando eles por virgulas *,* nem do *return*
sempre q coloca o valor *i[0]* a função já estará retornando esse valor para mim."""