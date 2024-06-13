n = 1
filtragem = []
while (n < 7):
    numeros = float(input())
    filtragem.append(numeros)
    n += 1
positivos = 0
for i in filtragem:
    if i > 0:
        positivos += 1
    else:
        continue
print(f'{positivos} valores positivos')