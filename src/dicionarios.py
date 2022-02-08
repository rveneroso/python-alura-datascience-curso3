# Dicionários são estruturas de dados mutáveis e não são ordenados. Isso faz sentido já que o acesso
# se faz pela chave, portanto não haveria necessidade de ordenação.

# Criando um dicionário
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

print(type(dados)) # Imprime <class 'dict'>

# Criando um dicionário a partir do resultado de uma função zip()
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]
dados = dict(zip(carros, valores))
print(dados)
