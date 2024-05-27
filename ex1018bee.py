reais = int(input('Insira o valor de reais para o troco: '))
notas = [200, 100, 50, 20, 10, 5, 2 , 1]
for i in range(len(notas)):
    if reais >= notas[i] :
        # o // representa a divisao inteira
        print(f'{reais//notas[i]} nota(s) de R${notas[i]}')
        # o  % fara o calculo do resto da divisao que sera decomposta nas notas subsequentes
        reais = reais % notas[i]
    else:
        print(f'0 nota(s) de R${notas[i]}')