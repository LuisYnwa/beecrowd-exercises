#A CORRIGIR
number1 = int(input())
number2 = int(input())
soma = 0
if number1 % 2 != 0:
    soma += number1
    if number2 % 2 != 0:
        soma += number2 + number1
    else:
        print(soma)
elif number2 % 2 != 0:
    soma += number2
    if number1 % 2 != 0:
        soma += number1 + number2
    else:
        print(soma)