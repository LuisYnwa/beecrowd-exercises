n = int(input())
fatorial_lista = []
fatorial = 1
for i in range(1, n+1):
    fatorial_lista.append(n)
    n -= 1
#print(fatorial_lista)

for z in fatorial_lista:
    fatorial *= z
print(fatorial)