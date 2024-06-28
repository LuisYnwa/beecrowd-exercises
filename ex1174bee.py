x_lista = []
for i in range(10):
    n = float(input())
    x_lista.append(n)

for i, valor in enumerate(x_lista): 
    if valor <= 10:
        print(f'A[{i}] = {valor}')