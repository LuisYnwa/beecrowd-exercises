number = int(input())
for i in range(number + 1):
    if i % 2 == 0 and i != 0:
        result = i * i
        print(f'{i}^2 = {result}')
    else:
        continue