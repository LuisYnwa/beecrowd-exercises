# "0" input pauses the program
while True:
    n = int(input())
    if n == 0:
        break
    print(f'{" ".join(map(str, range(1, n+1)))}') #range dentro do join para otimizar o tempo de execucao no beecrowd
    
