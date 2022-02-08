import pandas as pd
carros = ['Jetta Variant', 'Passat', 'Crossfox']

# Criação de uma Series a partir de uma lista
carros_series = pd.Series(carros)
print(carros_series)
'''
Imprime:
    0    Jetta Variant
    1           Passat
    2         Crossfox
    dtype: object
'''

# Criando um DataFrame a partir de uma lista de dicionários
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)
print(dataset)

# Criando um DataFrame a partir de uma fonte de dados externa.
dataset = pd.read_csv('../data/db.csv', sep=';')
print(dataset)