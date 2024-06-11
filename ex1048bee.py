salario = float(input())
def reajuste_salarial(s, p):
    novo_salario = s * p
    reajuste = novo_salario - s
    porcentagem = (p - 1) *100
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {porcentagem:.0f} %')

if(salario >= 0.0 and salario <= 400.00):

    reajuste_salarial(salario, 1.15)

elif(salario > 400.00 and salario <= 800.00):

    reajuste_salarial(salario, 1.12)

elif(salario > 800.00 and salario <= 1200.00):

    reajuste_salarial(salario, 1.10)

elif(salario > 1200.00 and salario <= 2000.00):

    reajuste_salarial(salario, 1.07)

elif salario > 2000.00:
    reajuste_salarial(salario, 1.04)