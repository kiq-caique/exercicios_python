"""Dicionários são formados por *chaves* e *valores* conforme exemplo abaixo. 
separados por  *:* e *,* cada chave tem um valor, e dentro de cada chava pode
ter outra chave e valor. Conforme exemplo a baixo  """
# d1 = {
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'tupla',
# }

# for k, v in d1.items():
#     print(k, v)
"""
clientes = {
    'cliente1' : {
        'nome1' : 'Carlos',
        'nome2' : 'Maria',
    },
    'cliente2' : {
        'nome1' : 'Reni',
        'nome2' : 'Thay',
    },
    'cliente3' : {
        'nome1' : 'Nilo',
        'nome2' : 'Thamara',
    },
}

for clientes_x, clientes_y in clientes.items():
    print(f'Lista {clientes_x}')
    for dados_x, dados_y in clientes_y.items(): #perceba q *dados_x* foi criado para descartar o 'nome1' e 'nome2' do print.
        print(f'\t{dados_y}')
"""

d1 = {
    'kiq': 'maria',
    'kiq': 'Mari',
    'kiq': 'aLICE',
}

for x, y in d1.items():
    print(f'{x}: {y[0:2]}')