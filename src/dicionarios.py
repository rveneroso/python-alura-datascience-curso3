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

# Para acessar o valor de um item para uma determinada chave
print(dados['Passat'])

# Verificando se uma determinada chave existe no dicionário:
print('Mercedes-Benz' in dados)

# Determinando o tamanho de um dicionário.
print(len(dados)) # len() retorna a quantiades de pares chave : valor presentes no dicionário.

# Adicionando um item ao dicionário
dados['Mercedes-Benz'] = 173000.0
print(dados)
'''
    {
        'Jetta Variant': 88078.64, 
        'Passat': 106161.94, 
        'Crossfox': 72832.16, 
        'DS5': 124549.07, 
        'Mercedes-Benz': 173000.0
    }
'''

# Removendo um item do dicionário
del dados['Passat']
print(dados)

dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}
print('acessorios' in dados['Crossfox'])
print('acessorios' in dados['Passat'])
print(dados['Crossfox']['valor'])
print(dados['Passat']['acessorios'][-1])

# Para atualizar um dicionário. A atualização permite a execução de mais de uma operação em
# um único comando. Por exemplo:
dados.update({'Passat': 106161.95, 'Fusca': 150000})
# O comando acima está atualizando o preço do veículo Passat e também inserindo o veículo
# Fusca ao dicionário.
print(dados)

# Copiando um dicionário.
novos_dados = dados.copy()

del novos_dados['Passat']
print(dados)
print(novos_dados)

# Para remover um item de um dicionário
valor_removido = novos_dados.pop('Crossfox')
print(valor_removido)
print(novos_dados)

# A linha abaixo resulta em erro já que não existe a chave 'Mercedes-Benz' no dicionário.
# valor_removido = novos_dados.pop('Mercedes-Benz')

# Para evitar o erro acima pode-se fazer:
valor_removido = novos_dados.pop('Mercedes-Benz','Chave não localizada')
print(valor_removido)

# Para eliminar todos os itens de um dicionário
novos_dados.clear()
print(novos_dados)
