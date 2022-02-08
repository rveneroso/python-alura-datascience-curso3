def media(lista):
  valor = sum(lista) / len(lista)
  return (valor, len(lista))

# A técnica de desempacotamento também pode ser aplicada ao retorno de uma função. No exemplo abaixo, temos:
# resultado = valor
# n = len(lista)
resultado, n = media([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(resultado,n)
