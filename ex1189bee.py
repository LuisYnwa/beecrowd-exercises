operacao = input().upper()
soma = 0
qde = 0

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for i in range(1, 11):  # Exclui a primeira e a última linha
    if i <= 5:
        for j in range(0, i):  # Elementos antes da diagonal principal na parte superior
            soma += matriz[i][j]
            qde += 1
    else:
        for j in range(0, 11 - i):  # Elementos antes da diagonal secundária na parte inferior
            soma += matriz[i][j]
            qde += 1
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/qde:.1f}')
