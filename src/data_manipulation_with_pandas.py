import pandas as pd
dataset = pd.read_csv('../data/db.csv', sep=';')
pd.set_option('display.max_rows',10000)

# Exibindo os tipos de dados contidos no dataset
# OBSERVAÇÃO: o pandas entende que str é object
print(dataset.dtypes)
'''
Nome              object
Motor             object
Ano                int64
Quilometragem    float64
Zero_km             bool
Acessórios        object
Valor            float64
'''

# Para gerar estatísticas descritivas sobre uma ou mais informações contidas no dataset
print(dataset[['Quilometragem','Valor']].describe())
'''
 Quilometragem          Valor
count     197.000000     258.000000
mean    58278.421320   98960.513101
std     35836.733259   29811.932305
min       107.000000   50742.100000
25%     27505.000000   70743.512500
50%     55083.000000   97724.380000
75%     90495.000000  124633.302500
max    119945.000000  149489.920000
'''

# Exibindo algumas informações sobre o dataset
print(dataset.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 258 entries, 0 to 257
Data columns (total 7 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Nome           258 non-null    object 
 1   Motor          258 non-null    object 
 2   Ano            258 non-null    int64  
 3   Quilometragem  197 non-null    float64
 4   Zero_km        258 non-null    bool   
 5   Acessórios     258 non-null    object 
 6   Valor          258 non-null    float64
dtypes: bool(1), float64(2), int64(1), object(3)
memory usage: 12.5+ KB
None
'''