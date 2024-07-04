matriz = []
indice = int(input())
soma_ou_media = input().upper()
soma = 0
for i in range(12):
    linha = []
    for j in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

for a in range(12):
    soma += matriz[a] [indice]

if soma_ou_media == 'S':
    print(f'{soma:.1f}')
elif soma_ou_media == 'M':
    print(f'{soma/12:.1f}')

    