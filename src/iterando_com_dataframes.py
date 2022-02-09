import pandas as pd

# Criando um DataFrame a partir de uma fonte de dados externa.
dataset = pd.read_csv('../data/db.csv', sep=';')

# Iterando sobre o dataframe e calculando a kilometragem média de veículos não zero km.
for index, row in dataset.iterrows():
  if(2019 - row['Ano'] != 0):
    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
  else:
    dataset.loc[index, 'Km_media'] = 0

print(dataset)