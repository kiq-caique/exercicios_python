from map import produtos, pessoas, lista

# nova_lista = filter(lambda x: x > 5, lista)
# print(nova_lista) 
#mais uma vez, filter e map retornam valores iterável, então convertemos em lista com 
# print(list(nova_lista))

#em listcomprehension ficaria assim: 
# nova_lista = [x for x in lista if x > 5]
# print(list(nova_lista))

nova_lista = filter(lambda x: x['preco'] > 25, produtos)

for produto in nova_lista:
    print(produto)

