# Crie uma lista vazia para armazenar os números
numeros = []

# Pergunte ao usuário quantos números ele deseja adicionar
quantidade = int(input("Quantos números você deseja adicionar? "))

# Adicione os números à lista
for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Encontre o menor valor
menor_valor = min(numeros)

# Encontre o maior valor
maior_valor = max(numeros)

# Calcule a soma dos valores
soma = sum(numeros)

# Imprima os resultados
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma}")