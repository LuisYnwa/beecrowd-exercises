i = 1
j = 7
inicio = 7
contador = 0
while i < 11 and contador <= 2:
    print(f'I={i} J={j}')
    j += j * 1.1
    if j == (inicio - 3):
        i += 2
        inicio += 2
        j = inicio

