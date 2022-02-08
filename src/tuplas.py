# Tuplas armazenam objetos de tipos variados

# Diferentes maneiras de se criar tuplas
tupla1 = 1, 2, 3
print(tupla1)

nome = 'Honda CBX 1000'
valor = 235000.0
tupla2 = (nome, valor)
print(tupla2)

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
print(nomes_carros)

# Acessando elementos de uma tupla
print(nomes_carros[0]) # Jetta Variant
print(nomes_carros[1]) # Passat
print(nomes_carros[-1]) # DS5

# Slicing de tuplas
print(nomes_carros[1:3]) # ('Passat', 'Crossfox')
print(nomes_carros[1:-1]) # Gera o mesmo resultado acima: ('Passat', 'Crossfox')

# Tuplas contendo tuplas
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
print(nomes_carros)

# Acessando um item da tupla contida na tupla
print(nomes_carros[-1][1]) # Imprime Gol
print(nomes_carros[-1][-1]) # Imprime C4

# Desempacotamento automático de tuplas
# O quinto elemento da tupla é outra tupla contendo 3 elementos.
carro_1, carro_2, carro_3, carro_4, sub_carros = nomes_carros;
print(carro_1)
print(carro_2)
print(carro_3)
print(carro_4)
print(sub_carros[0])
print(sub_carros[1])
print(sub_carros[2])

# Se for ignorar um ou mais itens em uma atribuição simultânea em tuplas deve-se utilizar o underscore
# na posição dos itens a serem ignorados.
# A linha abaixo ignora os itens de índice 0, 2 e 5
_, carro_2, _, carro_4, _ = nomes_carros;
print(carro_2) # Imprime Passat
print(carro_4) # Imprime DS5

# Para obter apenas um item de uma tupla pode-se utilizar a seguinte sintaxe:
_, carro, *_ = nomes_carros
print(carro) # Retorna Passat que é o item de índice 2.
# Na sintaxe acima, o *_ diz ao Python para ignorar todos os demais itens da tupla daquela posição em diante.

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

# A função zip cria um iterador com base em duas tuplas.
for item in zip(carros,valores):
    print(item)
    '''
    Irá imprimir:
    
    ('Jetta Variant', 88078.64)
    ('Passat', 106161.94)
    ('Crossfox', 72832.16)
    ('DS5', 124549.07)
    
    '''

# É possível também aplicar o desempacotamento diretamente sobre o resultado da função zip().
for carro, valor in zip(carros, valores):
    print(carro, valor)
    '''
    Irá imprimir:
    
    Jetta Variant 88078.64
    Passat 106161.94
    Crossfox 72832.16
    DS5 124549.07
  
    '''

# É possível também criar uma lista diretamente a partir do resultado da função zip
lista_carros = list(zip(carros,valores))
print(lista_carros)
# Imprime [('Jetta Variant', 88078.64), ('Passat', 106161.94), ('Crossfox', 72832.16), ('DS5', 124549.07)]
