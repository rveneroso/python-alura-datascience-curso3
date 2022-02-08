dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

# Obtém todas as chaves de um dicionário
print(dados.keys()) # Imprime dict_keys(['Crossfox', 'DS5', 'Fusca', 'Jetta Variant', 'Passat'])

for key in dados.keys():
    print(dados[key])

# Obtém todos os valores de um dicionário
print(dados.values()) # Imprime dict_values([72832.16, 124549.07, 150000, 88078.64, 106161.95])

for value in dados.values():
    print(value)

# Retorna uma lista de tuplas contendo chave : valor presentes no dicionário
lista_veiculos = dados.items()
print(lista_veiculos)
'''
Imprime:

dict_items([
    ('Crossfox', 72832.16), 
    ('DS5', 124549.07), 
    ('Fusca', 150000), 
    ('Jetta Variant', 88078.64), 
    ('Passat', 106161.95)
])
'''

# Dicionários também permitem o desempacotamento de dados diretamente:
for key, value in dados.items():
    print(f'O veículo {key} custa {value}')