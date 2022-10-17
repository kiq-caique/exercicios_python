"""
Operadores lógicos: and, or, not, in e not in.
"""
#(verdadeiro E verdadeiro) = Verdadeiro - precisa das 2 serem verdadeiras.
#(verdadeiro E falso) = Falso
comparacao1 and comparacao2 

#verdadeiro OU verdadeiro = Verdadeiro - apenas uma precisa atender a condição.
comparacao1 or comparacao2 

#No exemplo a baixo, o retorno seria: 'B é maior que A'.
#Trocando if por <if not> o retorno seria: 'A é maior que B'. mesmo A < B. isso se dá devido ao 'if not' 
a = 2
b = 3

if b > a: 
    print('B é maior que A.')
else:
    print('A é maior que B')  

if not b > a: 
    print('B é maior que A.')
else:
    print('A é maior que B')  

#No exemplo a baixo, "Car" esta contido na variável nome, o retorno seria: 'existe'
nome = "Carlos Henrique"

if 'Car' in nome:
    print('existe')
else:
    print('não exite')   

#No exemplo a baixo, "eu" NÃO esta contido na variável <nome>, o retorno seria: 'não existe'
nome = "Carlos Henrique"

if 'eu' not in nome:
    print('não exite')
else:
    print('existe')    