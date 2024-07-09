matriz = []
soma_ou_media = input().upper()
indice = int(input())
soma = 0
for i in range(12):
    linha = []
    for j in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

for a in range(12):
    soma += matriz[a] [a]#indices iguais para seguir as coordenadas diagonais que sempre sao iguais quando representadas na matriz

if soma_ou_media == 'S':
    print(f'{soma:.1f}')
elif soma_ou_media == 'M':
    print(f'{soma/12:.1f}')

    
