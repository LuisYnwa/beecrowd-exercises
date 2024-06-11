# A VERIFICAR NO BEECROWD
#a, b, c, d = map(int(), input().split())
import sys
a, b, c, d = map(int, input().split())
inicio_minutos = (a * 60) + c
termino_minutos = (b * 60) + d
resultado_minutos = termino_minutos - inicio_minutos

if inicio_minutos == termino_minutos:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    sys.exit()

elif resultado_minutos < 0:
    resultado_minutos = resultado_minutos + (24*60)

resultado_horas = resultado_minutos // 60
resultado_minutos = resultado_minutos % 60 #calcula o resto da divisao por 60 e adiciona a variavel, garantindo que seja menor que 60 minutos
print(f'O JOGO DUROU {resultado_horas} HORA(S) E {resultado_minutos} MINUTO(S)')
