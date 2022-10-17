from map import produtos, pessoas, lista

"""
A função *map* recebe como primeiro argumento uma função. Para isso iremos utiliza a
função *lambda*.A função *map* nao retorna uma lista pronta. Ela retorna um iterador
para vc iterar sobre esse elemento. Para visualizar como lista podemos fazer um type_cast
e mudar ela para uma lista. ex: print(list(nova_lista))
"""
#após a utilização de lambda, defino os critérios da função e no final.Então como 
#último argumento escolho a *lista* (pq é onde quero aplicar os critérios da função criada) 

# nova_lista = map(lambda x: x * 2, lista)  

# print(lista)
# print(nova_lista)
# print(list(nova_lista))

"""
Nesse caso a função map poderia ser substituida pela listcomprehension:

nova_lista = [x * 2 for x in lista]
nesse caso, a função map consegue mostrar os valores multiplicados devido a 
lista ser uma *lista*. Mas no caso dos dicionários *produtos* e *pessoas* 
ela não conseguiria fazer alterações nos valores sem def uma função antes.
"""
# def aumento_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p

#cria-se novos_produtos para diferenciar o *produtos* q ja existia. 
# novos_produtos = map(aumento_preco, produtos)  
precos = map(lambda p: p['preco'], produtos) 

for precos in produtos:
    print(precos)
"""para se obter somento os valores, vc deve fazer o seguinte:
    
    for x in precos:
        print(x)
"""
# for produto in novos_produtos:
#     print(produto)