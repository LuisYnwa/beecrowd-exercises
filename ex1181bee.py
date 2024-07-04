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
    for b in range(12):
        if a == indice:
            soma += matriz[a] [b]

if soma_ou_media == 'S':
    print(soma)
elif soma_ou_media == 'M':
    print(soma/12)

    