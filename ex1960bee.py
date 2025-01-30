def int_to_roman(input):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []

    for i in range(len(ints)):
        count = int(input / ints[i]) #count valida se o input eh menor que o valor ccorrespondente (i) na lista, se nao for resultara em 0
        result.append(nums[i] * count) #caso seja 0, ele ira multiplicar o correspondente (nums[i) com 0, por consequencia nao adicionando a lista result.
        #em caso do resultado da divisao for 1, ele ira adicionar a letra correspondente e ira avancar
        input -= ints[i] * count
    return ''.join(result)

n = int(input())

n = int_to_roman(n)

print(n)

#EXEMPLO DE DEBUG COM O NUMERO 666:
#for ints[2] = 500 e nums[2] = 'D':

#count = int(666 / 500) = 1

#result.append('D' * 1) = result.append('D') ➔ result = ['D']

#input -= 500 * 1 = 666 - 500 = 166


#for ints[8] = 100 e nums[8] = 'C':

#count = int(166 / 100) = 1

#result.append('C' * 1) = result.append('C') ➔ result = ['D', 'C']

#input -= 100 * 1 = 166 - 100 = 66


#for ints[10] = 50 e nums[10] = 'L':

#count = int(66 / 50) = 1

#result.append('L' * 1) = result.append('L') ➔ result = ['D', 'C', 'L']

#input -= 50 * 1 = 66 - 50 = 16b