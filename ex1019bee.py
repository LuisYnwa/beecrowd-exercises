segundos_inteiros = int(input('Insira os segundos totais: '))
horas = segundos_inteiros // 3600 #1 hora em segundos
resto_horas = segundos_inteiros % 3600
minutos = resto_horas // 60
segundos = resto_horas % 60
print(f'{horas}:{minutos}:{segundos}')
