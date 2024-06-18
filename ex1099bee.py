n = int(input())
for i in range(n):
    a, b = (map(int, input().split()))
    soma_impares = 0
    if b > a or b == a:
        for i in range(a+1, b):
            if i % 2 != 0:
                soma_impares += i
            else:
                continue
    else:
        for i in range(a-1, b, -1): #loop inverso com step no terceiro argumento para valores a > b
            if i % 2 != 0:
                soma_impares += i

    print(soma_impares)
    soma_impares = 0 
    