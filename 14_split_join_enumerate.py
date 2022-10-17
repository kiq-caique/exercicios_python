"""
  Strip - retira o espaçamento.
  Split - Dividir uma str
  Join - Juntar uma Lista #str
  Enumerate - Enumerar elementos da lista #iteráveis (não é interáveis é iterar 
  significa: Repetir ou dizer outra vez, Refazer ou fazer outra vez. Em Álgebra.
  Utilizar-se da iteração em valer-se do resultado de uma equação, através de
   sucessivos cálculos.)
"""
""" #Split
string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print( f'A palavra {valor} apareceu {lista1.count(valor)}x na frase' )

palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
    
print(f'A palavra que apareceu mais vezes é {palavra.upper()} ({contagem}x)')
"""
""" #Strip
for valor in lista2:
    print(valor.strip())
"""
""" #Join
string = "O Brasil é penta."
lista1 = string.split(' ')
string2 = ','.join(lista1)


print(string)
print(lista1)
print(string2)
"""
""" #Enumerate 
lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

"""