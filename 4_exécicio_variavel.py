"""
Exercício:
Criar variáveis para nome (str), idade (int), altura (float), peso (float), de uma pessoa.
Criar uma variável com o ano atual (int).
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pesoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-string (com duas casas decimais)
"""

nome = 'Carlos'
idade = 29
altura = 1.75
peso = 66.6
imc = peso/altura**2
ano_atual = 2022
nascimento = ano_atual - idade

print(f'{nome} tem {idade} de idade e mede {altura} tem imc de {imc:.2f} e nasceu no ano de {nascimento}')
