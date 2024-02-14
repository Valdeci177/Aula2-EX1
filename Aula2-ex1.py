# Criar uma lista vazia para armazenar os valores inseridos pelo usuário
valores = []

# Solicitar ao usuário que insira 10 valores
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Separar os números pares e ímpares em listas diferentes
numeros_pares = []
numeros_impares = []

for valor in valores:
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

# Exibir na tela os números pares e ímpares
print("Números pares:", numeros_pares)
print("Números ímpares:", tuple(numeros_impares))  # Convertendo para uma tupla para exibir na tela

# Calcular a quantidade de números pares e ímpares presentes na lista
quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)

# Calcular a soma de todos os números pares e ímpares
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

# Exibir na tela a quantidade e a soma dos números pares e ímpares
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)