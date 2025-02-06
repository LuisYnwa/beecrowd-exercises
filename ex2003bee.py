#acrescentar 1 hora de atraso 
#printar os minutos de atraso
#objetivo eh chegar as 8:00
#5:00 - 9:00
from datetime import datetime
import sys

for linha in sys.stdin:
    horario_acordar = linha.strip()
    if not horario_acordar:
        continue
        
    horario = datetime.strptime(horario_acordar, "%H:%M")
    hora_acordada = horario.hour
    minuto_acordado = horario.minute

    if hora_acordada == 7:
        print(f'Atraso maximo: {minuto_acordado}')

    elif hora_acordada > 7:
        atraso_horas = hora_acordada - 8
        atraso_final = (atraso_horas * 60) + minuto_acordado + 60  # Adiciona 1 hora de atraso
        print(f'Atraso maximo: {atraso_final}')

    else:   
        print('Atraso maximo : 0')
