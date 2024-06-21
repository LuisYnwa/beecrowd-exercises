grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
while True:
    inter, gremio = map(int, input().split())
    if inter > gremio:
        vitorias_inter += 1
        grenais +=1
    elif gremio > inter:
        vitorias_gremio +=1
        grenais +=1
    else:
        empates += 1
        grenais +=1
    novo_grenal = int(input('Novo grenal (1-sim 2-nao)'))
    if novo_grenal == 1:
        continue
    elif novo_grenal == 2:
        break
    elif novo_grenal == '':
        int(input('Novo grenal (1-sim 2-nao)'))
print(f'{grenais} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'empates:{empates}')
if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_gremio > vitorias_inter:
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')