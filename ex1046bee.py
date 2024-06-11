a, b = map(int, input().split())
#O TEMPO MAXIMO DE JOGATINA PRECISA SER DE 24 HORAS
#if a and b < 24:      #tratamento de erro de mais horas de um dia
if a == b:
    resultado = 24
elif a <= b: #EX: 2(a) - 16(b) = -14. Logo, so subtrair os valores do dia
    resultado = b - a
else:
    resultado = (24 - a) + b
    
print(f'O JOGO DUROU {resultado} HORA(S)')



