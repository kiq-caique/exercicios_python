"""
contador = 0
descontador = 10

while contador <=8:
    print (contador, descontador)

    contador += 1
    descontador -= 1
"""
"""
for e, r in enumerate(range(10, 1, -1)):
    print (e, r) 
"""


""" algoritimo do cpf
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
"validador de CPF"

cpf = input(' Digite seu CPF ')
novo_cpf = cpf[:9]
reverso = 10
total = 0

for index in range (19):
    if index >8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    print(cpf[index], index, reverso)
    
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)    

        if d > 9:
            d = 0
        total = 0 
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')


