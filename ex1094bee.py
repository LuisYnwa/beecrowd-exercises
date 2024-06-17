animal_lines = int(input())
rats = 0
bunnies = 0
frogs = 0
total = 0
for i in range(animal_lines):
    number, species = map(str, input().split())
    number = int(number)
    species = species.upper()
    if species == 'R':
        rats += number
        total += number
    elif species == 'C':
        bunnies += number
        total += number 
    if species == 'S':
        frogs += number
        total += number

percentage_bunnies = (bunnies / total) * 100.00
percentage_rats = (rats / total) * 100.00
percentage_frogs = (frogs / total) * 100.00

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {bunnies}')
print(f'Total de ratos: {rats}')
print(f'Total de sapos: {frogs}')
print(f'Percentual de coelhos: {percentage_bunnies:.2f} %')
print(f'Percentual de ratos: {percentage_rats:.2f} %')
print(f'Percentual de sapos: {percentage_frogs:.2f} %')