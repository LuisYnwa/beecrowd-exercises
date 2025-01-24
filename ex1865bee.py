tries = int(input())

for i in range(tries):
    name, newtons = input().split()
    if name == 'Thor':
        print('Y')
    else:
        print('N')
