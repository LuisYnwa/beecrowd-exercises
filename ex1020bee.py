idade_dias = int(input('Insira sua idade em dias: '))
anos = idade_dias // 365
resto_anos = idade_dias % 365
meses = resto_anos / 30
dias = resto_anos % 30
print(f'{anos} ano(s)')
#print(resto_anos)
print(f'{meses:.0f} mes(es)')
print(f'{dias} dia(s)')
