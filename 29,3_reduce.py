from map import produtos, pessoas, lista
from functools import reduce

"""
abaixo temos um exemplo onde irá somar todos os itens de uma lista

acumula = 0
for item in lista:
    acumula += item

print(acumula)

para a funçao *reduce* ficaria:

soma_lista = reduce (lambda x, i: i + x, lista, 0) 
print(soma_lista)
para a expressão acima temos o seguinte:

lambda x = função
i: i + x = oq a funçao irá fazer nesse caso esta pegando x como um acumulador e
           somando o i q é o item de uma lista, dai esse valor será guardado no x
           onde será passado a expressão para o próximo item da lista.
        
        lista = [1, 2, 3]
        x = 2
        entao seria : 2+1 = 3
                      3+2 = 5 
                      5+3 = 8 resultado final.

lista = de onde estou puxando os itens
0 = de onde estou partindo.
"""
soma_precos = reduce(lambda x, y: y['preco'] + x, produtos, 0)
print(round(soma_precos, 2))
