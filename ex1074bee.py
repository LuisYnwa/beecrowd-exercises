number = int(input())
#contador = 1
for i in range(number):
    n = int(input())
    if n > 0 and n % 2 == 0:
        print('EVEN POSITIVE')
    elif n < 0 and n % 2 == 0:
        print('EVEN NEGATIVE')
    elif n > 0 and n % 2 != 0:
        print('ODD POSITIVE')
    elif n < 0 and n % 2 != 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')

    #contador += 1