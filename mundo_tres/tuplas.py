# Criando uma tupla
tupla1 = (1, 2, 3)
print(tupla1)

# Tupla com diferentes tipos de dados
tupla2 = ('maçã', 3.14, True)
print(tupla2)

# Acessando elementos
print(tupla1[0])  # Saída: 1

# Tuplas são imutáveis
# tupla1[0] = 10  # Isso gera um erro

# Desempacotando tuplas
a, b, c = tupla1
print(a, b, c)

# Tupla com um único elemento (note a vírgula)
tupla3 = (5,)
print(tupla3)

# Concatenando tuplas
tupla4 = tupla1 + tupla3
print(tupla4)

# Verificando se um elemento está na tupla
print(2 in tupla1)  # Saída: True