sum = 0
sequence = []
n1, n2 = map(int, input().split())
while n1 != 0 and n2 != 0:
    sum = 0
    if n1 > n2:
        for i in range (n2, n1+1):
            sequence.append(i)
            sum += i
        print(f'{" ".join(map(str, sequence))} Sum={sum}')
        sequence.clear()
    elif n1 < n2:
        for i in range(n1, n2+1):
            sequence.append(i)
            sum += i
        print(f'{" ".join(map(str, sequence))} Sum={sum}')
        sequence.clear()

    n1, n2 = map(int, input().split())