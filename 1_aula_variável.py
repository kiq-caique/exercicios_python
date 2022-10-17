"""
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
"""
nome = "Carlos"
idade = 29
altura = 1.75
e_maior = idade > 18
peso = 66
imc = peso/altura**2


print(nome, "tem", idade, 'anos de idade e seu imc', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #:.2f (significa que teremos 2 casas depois da vírgula e o f significa q é um numero flutuante-float)
print('{} tem {} anos de idade e seu imc é {:.4f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2:.3f}'.format(nome, idade, imc))

