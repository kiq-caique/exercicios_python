"""
Listas em Python 
fatiamento
lista = [começo : stop : step/pulo]
append = l2.append('A') adiciona a str A no final da lista l2 
insert = l2.insert (0, "banana") adiciona a str banana no indice 0 da lista l2
pop = exclui o ultimo da lista
del = del(l2[3:6]) exclui os elementos correspondente aos indices 3,4 e 5 da lista l2
clear = 
extend = l1.extend(l2) irá juntar 2 listas já existente
+ = adiciona uma lista dentro da outra bem parecido com .extend
min, max = print(min(l1)) irá mostrar o menor VALOR (e ñ o menor indice) da lista l1
range = list(range(1,10)) irá mostrar 0,1,2,3,4,5,6,7,8,9 

print(lista[2]) #irá aparecer o indice correspondente 
print(lista[0:3]) #irá aparecer os indices de 0 até o indice correspondente ao 2
"""
secreto = "perfume"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'    

    if secreto_temporario == secreto:
        print("Que legal, VOCÊ GANHOU!!!! A palavra era {secreto_temporario}.")
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    
    print(f'Você possui {chances} chances!')
    print()
