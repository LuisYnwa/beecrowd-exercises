number = int(input())
for i in range(11):
    if i != 0:
        result = i * number
        print(f'{i} x {number} = {result}')
    else:
        continue