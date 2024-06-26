#INCOMPLETO
test_cases = int(input())
count = 0
odds = []
while count < test_cases:
    a, b = map(int, input().split())
    if a % 2 == 0:
        a+= 1 # transforma a variavel em impar 
        for i in range(1, b*2): 
            if a % 2 != 0:
                odds.append(a)
                a+= 1
            else:
                a+= 1
                continue
    else:
        for i in range(1, b*2): #b dobrado para pegar os numeros impares do b original (ja que impares serao a metade da quantidade de numeros)
            if a % 2 != 0:
                odds.append(a)
                a+= 1 
            else:
                a+= 1
                continue
    count += 1
    print(sum(odds))
    odds.clear()