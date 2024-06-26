cont = 0
years = 0
test_cases = int(input())
while cont < test_cases:
    population_a, population_b, gr_a, gr_b = map(float, input().split())
    while population_a <= population_b:
        population_a += int((population_a * gr_a) / 100)
        population_b += int((population_b * gr_b) / 100)
        years += 1 # 1 ano a mais para cada vez que o pai a nao passar a populacao do pais b
    if years > 100:
            print('Mais de 1 seculo.')
    else:
        print(f'{years} anos.')
    years = 0
    cont += 1
