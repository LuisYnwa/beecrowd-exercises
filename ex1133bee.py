x = int(input())
y = int(input())
if x > y:
    x, y = y, x #serve para garaantir que o numero menor sempre stara no x ja que o enunciado pede que os numeros sejam mostrados em ordem crescente
for i in range(x+1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
    else:
        continue
