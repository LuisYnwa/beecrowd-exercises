chances = int(input())
for i in range(chances):
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        result = x / y
        print(f'{result:.1f}')