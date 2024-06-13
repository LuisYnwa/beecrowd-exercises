pares = 0
impares = 0 
positivos = 0
negativos = 0
n = 1
while (n < 6):
    numero = int(input())
    n += 1
    if numero % 2 == 0:
        pares += 1
        if numero > 0:
            positivos += 1
            continue
        elif numero < 0:
            negativos += 1  
            continue
    elif numero % 2 != 0:
        impares += 1
        if numero > 0:
            positivos += 1
            continue
        elif numero < 0:
            negativos += 1  
            continue
    

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')