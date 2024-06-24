number = int(input())
pum = 1
print(f'{pum} {pum} {pum}')
print(f'{pum} {pum+1} {pum+1}')
while pum < number:
    pum += 1
    pum2 = int(pow (pum, 2))
    pum3 = int(pow (pum, 3))
    print(f'{pum} {pum2} {pum3}')
    print(f'{pum} {pum2+1} {pum3+1}')
