cont = 0
media = 0
while cont < 2:
    n = float(input())
    if n >= 0 and n <= 10:
        media += n
        cont += 1
        if cont == 2:
            media_final = media / 2  
            print(f'media = {media_final:.2f}')
            comando = int(input('novo calculo (1-sim 2-nao)'))
            if comando == 1:
                cont = 0
                media = 0
                continue
            elif comando == 2:
                break
            else:
                #comando = int(input('novo calculo (1-sim 2-nao)'))
                while comando != 1 and comando != 2:
                    comando = int(input('novo calculo (1-sim 2-nao)'))
                    if comando == 1: 
                        cont = 0
                        media = 0
                        continue
    else:
        print('nota invalida')

  
