number = float(input())
descending = [number, ]
print(f'N[0] = {number:.4f}')
for i in range(1, 100):
    count = 0

    while count < number:
        number /= 2
        descending.append(number)
        count += 1
        
    print(f'N[{i}] = {descending[i]:.4f}')