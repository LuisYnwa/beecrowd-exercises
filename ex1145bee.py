#INCOMPLETO
a, b = map(int, input().split())
print(f'{a - 2} {a - 1} {a}')
teste1 = a
a += 1
for i in range(a, b-1):
    print(f'{teste1} {teste1+1} {teste1+2}')
    teste1 += 3
    if a == b-1:
        exit()