number1 = int(input())
number2 = int(input())
soma = 0
if number1 % 2 != 0:
    soma += number1
    if number2 % 2 != 0:
        soma += number2 
        print(soma)

    else:
        print(soma)

elif number2 % 2 != 0:
    soma += number2
    if number1 % 2 != 0:
        soma += number1 
        print(soma)
    else:
        print(soma)
