count = 0
lines = int(input())

while count < lines:
    n = int(input())
    eh_primo = True

    for i in range(2, int(n**0.5) + 1): #uso da raiz quadrada para verificar apenas os primeiros, melhorando a eficiencia do codigo por n precisar iterar ate o n final 
        if n % i == 0:
            eh_primo = False
            break #sem necessidade do else por conta da logica booleana

    if eh_primo:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')

    count += 1