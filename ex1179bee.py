#read 15 numbers
# array even and array odd com 5 espacos cada
#printar todos os que sobraram juntos com suas respectivas listas no final
even = []
odd = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        even.append(n)
        if len(even) == 5:
            for i, valor in enumerate(even):
                print(f'par[{i}] = {valor}')
            even.clear()
    else:
        odd.append(n)
        if len(odd) == 5:
            for i, valor in enumerate(odd):
                print(f'impar[{i}] = {valor}')
            odd.clear()
for i, valor in enumerate(odd):
    print(f'impar[{i}] = {valor}')
for i, valor in enumerate(even):
    print(f'par[{i}] = {valor}')

