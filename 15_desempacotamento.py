lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista = lista  # *cria uma lista com os resto dos valores
print(n2, outra_lista)