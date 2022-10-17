m = int(input('Número de linhas que sua matriz terá? '))
n = int(input('Número de colunas que sua matriz terá? '))

mat = [[0 for x in range(n)] for x in range(m)]

for i in range(0,m):
    for j in range(0, n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))
print()
print('Matriz Digitada: ')
for i in range(0, m):
    for j in range(0,n):
        print(f'{mat[i][j]} ', end='')
    print()