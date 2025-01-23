operacao = input().upper()
soma = 0
lin = 12
qde = 0

matriz = [] #constrói a matriz (12x12)
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for c in range(12): #mexe nas linhas
    lin -= 1
    for j in range(12): #mexe nas colunas
        if j > lin and j < c:
            soma += matriz[c][j]
            qde += 1

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/qde:.1f}')
