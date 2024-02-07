#Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.

carrinho_de_compras = {} 

carrinho_de_compras['uva'] = 6
carrinho_de_compras['tangerina'] = 5
carrinho_de_compras['ameixa'] = 3
carrinho_de_compras['milho verde'] = 1
carrinho_de_compras['ervilha'] = 1
carrinho_de_compras['guardanapo'] = 2
carrinho_de_compras['papel aluminio'] = 1
carrinho_de_compras['arroz'] = 2
carrinho_de_compras['atum'] = 1

print("Carrinho de Compras:")
for produto, quantidade in carrinho_de_compras.items():
    print(f"{produto}: {quantidade}")

total = sum(carrinho_de_compras.values())
print(f"Total do Carrinho: {total}")
