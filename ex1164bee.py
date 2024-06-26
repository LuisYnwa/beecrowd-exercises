count = 0
test_cases = int(input())
perfect_count = 0
while count < test_cases:   
    x = int(input())
    if x == 1:
        print('1 nao eh perfeito')
    for i in range(1, x+1):
        if perfect_count > x: #contador faz a soma total ao inves de utilizar listas
            print(f'{x} nao eh perfeito')
            break
        elif perfect_count == x:
            print(f'{x} eh perfeito')
            break
        else:
            perfect_count += i

    count += 1
    perfect_count = 0

