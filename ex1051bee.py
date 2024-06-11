salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')

elif salario > 2000.00 and salario <= 3000.00:
    calculo1 = (salario - 2000.00) * 0.08
    print(f'R$ {calculo1:.2f}')

elif salario > 3000.00 and salario <=4500.00:
    calculo1 = (salario - 2000.00) * 0.18
    calculo2 = 0.08 * 1000
    print(f'R$ {calculo1 + calculo2:.2f}')

else:
    calculo01 = 0.08 * 1000
    calculo02 = 0.18 * 1500
    calculo03 = 0.28 * (salario - 4500)
    print('R$ {:.2f}'.format(calculo01 + calculo02 + calculo03))