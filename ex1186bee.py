matriz = []
soma_ou_media = input().upper()
soma = 0
contador = 0
for i in range(12):
    linha = []
    for j in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

for a in range(12):
    for j in range(12 - a, 12):
        soma += matriz[a] [j]
        contador += 1

if soma_ou_media == 'S':
    print(f'{soma:.1f}')
elif soma_ou_media == 'M':
    print(f'{soma/contador:.1f}')


    
