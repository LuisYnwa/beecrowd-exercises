choices = int(input())
numbers_int = []
numbers = input()
numbers_str = numbers.split()

for n in numbers_str:
    numbers_int.append(int(n))

print(f'Menor valor: {min(numbers_int)}')
print(f'Posicao: {numbers_int.index(min(numbers_int))}')