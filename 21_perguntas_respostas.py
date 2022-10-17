print()
print('Para as perguntas a baixo, digita a letra correspondente a alternativa que deseja escolher. Somente a letra!! ')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {'a': '4', 'b': '6', 'c': '5',},
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Qual é a capital do Brasil? ',
        'respostas': {'a': 'Rio de Janeiro', 'b': 'Curitiba', 'c': 'Brasilia',},
        'resposta_certa': 'c',
    },
}

print() #somente para ter um espaçamento 
resposta_certas = 0
for x, y in perguntas.items(): #itemS com *s* no final para acessar chaves e perguntas
    print(f'{x}: {y["pergunta"]}')

    print('Respostas: ')
    for rx, ry in y['respostas'].items():
        print(f'[{rx}]: {ry}')


    resposta_usuario = input('Sua resposta: ')
    
    if resposta_usuario == y['resposta_certa']:
       print('EHHHH!!!! Você ACERTOU!!!!')
       resposta_certas += 1
    else:
        print('VIISHHH!!! Você precisa ESTUDAR!!!')
    
    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas / qtd_perguntas * 100

print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}%')