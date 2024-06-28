reverse = []

for l in range(20):
    n = int(input())
    reverse.append(n)

for i in range(20):
    print(f'N[{i}] = {reverse[19 - i]}') #19-i vai reduzir a casa de selecao de acordo com o indice da vez, enquanto o primeiro indice vai colocar em ordem de 0 a 19