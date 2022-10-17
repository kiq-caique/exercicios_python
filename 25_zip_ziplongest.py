"""
Zip - Unindo iteráveis
Zip_longest - Itertools (no caso do exemplo a baixo usamos um count, nesse caso
o count com zip_longest nao teria fim, TRAVA O PC!)
"""
from itertools import zip_longest, count

### Código
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice,cidades, estados)
cidades_estados1 = zip(indice, cidades, estados) 
cidades_estados2 = zip_longest(cidades, estados, fillvalue='Estado') 

# print(list(cidades_estados))
# print(list(cidades_estados1))
# print(list(cidades_estados2))

for indice, estados, cidades in cidades_estados1: # ONDE TEM ZIP E NÃO ZIP_LONGEST
    print(indice, estados, cidades)