X, Y = map(int, input().split())

# Inicializa um contador para controlar os números impressos por linha
count = 0

# Itera de 1 até Y (inclusive)
for i in range(1, Y + 1):
    # Imprime o número atual
    print(i, end=" ")

    # Incrementa o contador
    count += 1

    # Verifica se X números foram impressos na linha atual
    if count == X:
        print()  # Quebra de linha
        count = 0  # Reseta o contador