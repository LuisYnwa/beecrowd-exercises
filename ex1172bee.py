numbers_list = []
for i in range (0, 10):
    n = int(input())
    if n > 0:
        n = str(n)
        #numbers_list.append(n)
        print(f'X[{i}] = {n}')
    else:
        #numbers_list.append('1')
        print(f'X[{i}] = {1}')
        continue
    