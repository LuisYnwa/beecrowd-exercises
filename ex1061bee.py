#min_seg = 60
#hora_seg = 3600
#dia_seg = 86400

dia1 = int(input().split()[1])
hora1, min1, seg1 = map(int, input().split(":"))
tempo1 = seg1 + min1 *60 + hora1 * 60 * 60 + dia1 * 24 * 60 *60 #converte tudo para segundos 

dia2 = int(input().split()[1])
hora2, min2, seg2 = map(int, input().split(":"))
tempo2 = seg2 + min2 *60 +  hora2 * 60 * 60 + dia2 * 24 * 60 *60
#faz a diferenca entre segundos do tempo  inicial e final
diferenca = tempo2 - tempo1

resultado_dias = diferenca // (24 * 60 * 60) #24 horas x 1 hora em segundos
diferenca = diferenca % (24 * 60 * 60) #resto das dias retornam para calcular as horas

resultado_horas = diferenca // (60 * 60)
diferenca = diferenca % (60 * 60) #resto das horas retornam para continuar os minutos etc.

resultado_minutos = diferenca // 60
diferenca = diferenca % 60

diferenca_segundos = diferenca

print(f'{resultado_dias} dia(s)')
print(f'{resultado_horas} hora(s)')
print(f'{resultado_minutos} minuto(s)')
print(f'{diferenca_segundos} segundo(s)')

