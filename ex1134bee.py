#1. Alcohol 2. Gasoline 3. Diesel 4. End
alcohol = 0
gasoline = 0
diesel = 0
try:
    while True:
        customer = int(input())
        if customer == 1:
            alcohol += 1
        elif customer == 2:
            gasoline += 1
        elif customer == 3:
            diesel += 1
        elif customer == 4:
            break

except EOFError:
    pass

print('MUITO OBRIGADO')
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {diesel}')