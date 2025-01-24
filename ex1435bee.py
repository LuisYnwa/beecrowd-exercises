def build_array(n): #cria a matriz 
    array = [[0]*n for _ in range(n)] #cria linhas com sublinhas de 0 na ordem n x n
    
    for i in range(n): #altera a linha da matriz
        for j in range(n): #altera a coluna da matriz
            array[i][j] = min(i, j, n-i-1, n-j-1) + 1 #min garante que os valores cresçam em direção ao centro da matriz
            #i: A posição atual na linha
            #j: A posição atual na coluna
            #n-i-1: A distância da posição atual até a última linha
            #n-j-1: A distância da posição atual até a última coluna
            #+ 1: Adiciona 1 para começar a contagem a partir de 1 em vez de 0
    
    return array

def print_array(array):
    for row in array:
        print(" ".join(f"{val:>3}" for val in row)) #join é usado para criar o espaço entre os números da matriz
        #f"{val:>3}" formata o numero como " 1" na matriz
        # for val in row itera sobre cada valor em cada linha da matriz
    print()

while True:
    num = int(input())
    if num == 0:
        break
    else:
        result_array = build_array(num)
        print_array(result_array)
