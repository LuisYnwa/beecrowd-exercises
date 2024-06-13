n = 1
valores_pares = 0
while (n < 6):
    numero = float(input())
    n += 1
    if numero % 2 == 0:
        valores_pares += 1
    else:
        continue
print(f'{valores_pares} valores pares')