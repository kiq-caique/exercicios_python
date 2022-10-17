# input te retorna o valor em <str> já o len retorna em <int>, isso permite fazer opreções matemáticas com len

usuario = input ('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))
if qtd_caracteres < 6:
    print('Numero de caracteres menor que o mínimo, por favor, insira um usuário com 6 ou mais caracteres')
else:
    print('Usuário cadastrado')    