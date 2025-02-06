test_cases = int(input())
for i in range(test_cases):
    years_user = int(input())
    result = 2015 - years_user
    if result <= 0:
        print(f'{abs(result) + 1} A.C.') #abs para formatar o numero e tirar o sinal de ' - '
    else:
        print(f'{result} D.C.')