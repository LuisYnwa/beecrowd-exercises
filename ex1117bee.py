cont = 0
media = 0
while cont < 2:
    n = float(input())
    if n >= 0 and n <= 10:
        media += n
        cont += 1
    else:
        print('nota invalida')

media_final = media / 2    
print(f'media = {media_final:.2f}')