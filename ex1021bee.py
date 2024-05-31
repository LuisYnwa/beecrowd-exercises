reais = float(input('Insira o valor de reais incluindo os centavos para o troco: '))
notas = [200, 100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
for i in range (len(notas)):
    if reais >= notas[i]:
        print(f'{reais//notas[i]:.0f} nota(s) de R${notas[i]:.2f}')
        reais %= notas[i] #responsavel por reservar os centavos para o proximo loop ao final da lista de notas
    else:
        print(F'0 notas de R${notas[i]:.2F}')

for i in range(len(moedas)):
    if reais >= moedas[i]:
        print(f'{reais//moedas[i]:.0f} moeda(s) de R${moedas[i]:.2f}')
        reais %= moedas[i]
    else:
        print(f'0 moedas de R${moedas[i]:.2F}')