even = []
x = 1
while x != 0:
    x = int(input())
    if x == 0: # condicional para parar o loop precisa ficar em primeiro antes do while loop
        break
    while len(even) < 5:
        if x % 2 == 0:
            even.append(x)
        x += 1
    print(sum(even))
    even.clear()