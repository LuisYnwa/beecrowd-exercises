#INCOMPLETO
test_cases = int(input())
count = 0
odds = []
while count < test_cases:
    a, b = map(int, input().split())
    if a % 2 == 0:
        a += 1
        for i in range(a, b): # 1 no lugar do a se n for
            if i % 2 != 0:
                odds.append(i)
            else:
                continue
    else:
        for i in range(a, b): # 1 no lugar do a se n for
            if i % 2 != 0:
                odds.append(i)
            else:
                continue
    count += 1
    print(sum(odds))