import pandas as pd

# Criando um DataFrame a partir de uma fonte de dados externa.
dataset = pd.read_csv('../data/db.csv', sep=';')

# Exibe os 5 primeiros elementos do dataset
print(dataset.head())

# Recuperando uma coluna específica do dataset. Lembrando que o índice é exibido junto com a coluna selecionada.
print(dataset['Valor'])

# O comando acima retorna uma Series do Panda.
print(type(dataset['Valor'])) # Imprime <class 'pandas.core.series.Series'>

# Ao se recuperar uma coluna do dataset, se em vez de um par de colchetes forem usados dois, o retorno
# será um DataFrame
print(dataset[['Valor']])
print(type(dataset[['Valor']])) # Imprime <class 'pandas.core.frame.DataFrame'>

# Os critérios para a recuperação de elementos a partir dos índices em DataFrames são os mesmos utilizados
# para listas, tuplas e nparrays.
print(dataset[0:3])
'''
Imprime
     Nome  ...      Valor
    0  Jetta Variant  ...   88078.64
    1         Passat  ...  106161.94
    2       Crossfox  ...   72832.16
'''

# A linha abaixo altera o índice do DataFrame para que seja a coluna Nome. Até aqui o índice era o padrão, ou
# seja: 0 para o primeiro elemento, 1 para o seguinte and so on.
dataset.set_index('Nome', inplace=True)
# Agora é possível recuperar as informações relacionadas a um veículo em particular através de seu nome.
print(dataset.loc['Passat'])
# Se for recuperado apenas um elemento, o tipo de retorno é object. Porém, se forem recuperados dois ou mais
# elementos, o tipo de retorno passa a ser outro DataFrame.
print(dataset.loc[['Passat', 'Carens']])
# Para retornar apenas um conjunto de colunas dos elementos:
print(dataset.loc[['Passat', 'Carens'], ['Motor', 'Valor']])
# Para retornar apenas as colunas Motor e Valor para todas as linhas:
print(dataset.loc[:, ['Motor', 'Valor']])

# O método iloc é semelhante ao loc porém, ele só opera com índices numéricos. Por exemplo:
print(dataset.iloc[1:4, [0, 5, 2]])
'''
Imprime:

                    Motor      Valor  Quilometragem
Nome                                               
Passat       Motor Diesel  106161.94         5712.0
Crossfox  Motor Diesel V8   72832.16        37123.0
DS5       Motor 2.4 Turbo  124549.07            NaN

'''