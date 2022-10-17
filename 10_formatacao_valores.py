"""
Formatando valores com modificadores

:s - Texto (str)
:d - Inteiros (int)
:f - Numeros de ponto flutuantes (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERES) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1/num_2
#print( '{:.2f}'.format(divisao) )
#print( f'{divisao:.2f}' )