n = 1
media_positivos = 0
filtragem = []
while (n < 7):
    numeros = float(input())
    filtragem.append(numeros)
    n += 1
positivos = 0
for i in filtragem:
    if i > 0:
        positivos += 1
        media_positivos += i
    else:
        continue
media_positivos = media_positivos / positivos
print(f'{positivos} valores positivos')
print(f'{media_positivos:.1f}')