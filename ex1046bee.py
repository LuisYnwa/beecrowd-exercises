a, b = map(int, input().split())
#O TEMPO MAXIMO DE JOGATINA PRECISA SER DE 24 HORAS
#if a and b < 24:      #tratamento de erro de mais horas de um dia
if b - a < 24:
    resultado = (24 - a) + b
    print(f'O JOGO DUROU {resultado} HORA(S)')


