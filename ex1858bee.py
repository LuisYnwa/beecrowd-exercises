#pegar o(s) numero(s) de menor valor da lista
#printar a posicao dela na lista na ordenacao normal (1,2,3...)
#tentar sem a verificacao se os numeros que o usuario colocou correspondeu ao primeiro input

attempts = int(input())
numbers = list(map(int, input().split()))
min_list = min(numbers)
list_index = numbers.index(min_list)
list_index += 1
print(list_index) 