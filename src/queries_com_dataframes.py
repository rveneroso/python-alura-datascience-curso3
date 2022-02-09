import pandas as pd

# Criando um DataFrame a partir de uma fonte de dados externa.
dataset = pd.read_csv('../data/db.csv', sep=';')

# Se o rótulo de uma coluna em um dataset for um nome simples, é possível recuperar diretamente as informações
# daquela coluna simplesmente fazendo o seguinte:
print(dataset.Motor)

# Se for realizada uma consulta baseada numa condição específica, o resultado será uma matriz booleana.
# Por exemplo: para selecionar todos os veículos cujo tipo de motor ser 'Motor Diesel' fazemos:
print(dataset.Motor == 'Motor Diesel')
# Deve-se observar que o resultado não se restringe apenas aos veículos cujo motor ser 'Motor Diesel'. A query
# irá retornar TODOS os elementos. Porém, aqueles cujo motor se 'Motor Diesel' terão True na coluna Motor ao
# passo que os demais terão False.
'''
Imprime:

Name: Motor, Length: 258, dtype: object
0      False
1       True
2      False
3      False
4      False
       ...  
253    False
254    False
255    False

'''

# É possível utilizar uma matriz booleana para filtrar os elementos de um DataFrame:
select = dataset.Motor == 'Motor Diesel'
print(dataset[select]) # No caso do dataset aqui sendo usado, irá retornar apenas 26 itens.

# Selecionando todos os veículos que são motor a diesel e zero km
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km)])
'''
Imprime:

                   Nome  ...      Valor
60               Sorento  ...   81399.35
78           Cielo Hatch  ...  145197.70
124                Camry  ...  138597.27
189  Aston Martin Virage  ...   97290.18
237         Série 7 Sedã  ...   67539.79

'''

# Consulta acima também pode ser feita utilizando-se o método query():
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))