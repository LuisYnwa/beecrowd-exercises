a, b = map(int, input().split())
print(f'{a - 2} {a - 1} {a}')
teste1 = a
a += 1
cont = 0
while teste1 < b:
    print(f'{teste1+1} {teste1+2} {teste1+3}')
    teste1 += 3
    cont += 1