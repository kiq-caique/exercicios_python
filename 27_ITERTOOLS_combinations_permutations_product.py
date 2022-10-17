'''
Combinations - ordem importa ex: ('luiz', 'andré') é = ('andré', 'luiz') então só aparece 1 deles
Permutations - ordem nao importa ('luiz', 'andré') são diferentes ('andré', 'luiz') aparece os 2
* AMBOS combinations e permutations não repetem valores únicos

Product - ordem importa e repete valores únicos ('luiz', 'luiz') e ('andré', 'andré')
irão aparecer além de ('luiz', 'andré') e ('andré', 'luiz')

'''
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2): #para product fica product(pessoas, repeat=2)
    print(grupo)