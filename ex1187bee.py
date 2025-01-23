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

# Calcula a soma para a área verde em X
for i in range(5):
    for j in range(i + 1, 11 - i):
        soma += matriz[i][j]
        contador += 1

if soma_ou_media == 'S':
    print(f'{soma:.1f}')
elif soma_ou_media == 'M':
    media = soma / contador
    print(f'{media:.1f}')

    
