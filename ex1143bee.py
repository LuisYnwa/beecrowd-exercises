from math import pow
number = int(input())
#cont = 0
pum = 1
print(f'{pum} {pum} {pum}')
#pum += 1
while pum < number: # o segredo desse exercicio e exponenciar na segunda coluna ao quadrado e na terceira ao cubo
    pum += 1
    pum2 = int(pow (pum, 2))
    pum3 = int(pow (pum, 3))
    print(f'{pum} {pum2} {pum3}')
