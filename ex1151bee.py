number = int(input())
fibonacci = [0, 1]

for i in range(1, number + 1):
    fib_soma = fibonacci[-2]
    fib_soma2 = fibonacci[-1]
    fibonacci.append(fib_soma2 + fib_soma)

fibonacci = fibonacci[:-2]
print(f'{" ".join(map(str, fibonacci))}')