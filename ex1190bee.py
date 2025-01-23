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

for i in range(1, 11):  
    if i <= 5:
        for j in range(12 - i, 12): 
            soma += matriz[i][j]
            qde += 1
    else:
        for j in range(12 - (11 - i), 12):  
            soma += matriz[i][j]
            qde += 1

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/qde:.1f}')
