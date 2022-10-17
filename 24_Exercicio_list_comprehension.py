carrinho = [] 
carrinho.append(('Produto1', 30.5))
carrinho.append(('Produto2', '20.1'))
carrinho.append(('Produto3', 50))

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)

