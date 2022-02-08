class Pessoa:
    def __init__(self, nome, idade, naturalidade):
        self._nome = nome
        self._idade = idade
        self._naturalidade = naturalidade

    def __str__(self):
        return (f'A pessoa {self._nome} tem {self._idade} anos e nasceu na cidade de {self._naturalidade}')


pessoa1 = Pessoa('Renato Veneroso', 54, 'Belo Horizonte')
pessoa2 = Pessoa('Simome de lima', 48, 'Nova Lima')
pessoa3 = Pessoa('Nicolas Lima Veneroso', 10, 'Belo Horizonte')

# Cria um dicionário e adiciona os 3 objetos Pessoa criados acima a ele.
pessoas = {}
pessoas['pessoa1'] = pessoa1
pessoas['pessoa2'] = pessoa2
pessoas['pessoa3'] = pessoa3

# Faz uma cópia do dicionário pessoas. Observação: embora seja feita uma cópia do dicionário pessoas, os objetos
# contidos em pessoas e pessoas_copia são os mesmos. Assim, alterações feitas nos objetos Pessoa usando qualquer
# um dos dicionários resultará em alterações diretamente nos objetos. É o comportamento padrão já verificado em
# listas.
pessoas_copia = pessoas.copy()

# Altera a naturalidade de pessoa1 usando o dicionário pessoas_copia
pessoas_copia['pessoa1']._naturalidade = 'São Lourenço'

print(pessoa1)
print(pessoa2)
print(pessoa3)