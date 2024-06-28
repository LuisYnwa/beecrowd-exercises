x = []
n = int(input())

for i in range(10):
    x.append(n) #nesse exercicio nao eh necessario indicar o local para o append ja que naturalmente ele vai ficar um valor a frente na lista
    n *= 2

for i in range(10):        
    print(f'N[{i}] = {x[i]}')