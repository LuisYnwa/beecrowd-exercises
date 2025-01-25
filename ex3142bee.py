import sys
def col_to_num(col):
    num = 0
    for char in col:
        if char < 'A' or char > 'Z':
            return "Essa coluna nao existe Tobias!"
        num = num * 26 + (ord(char) - ord('A') + 1) #num * 26 eh usado para criar a base 26
        #ord mostra o valor unicode da letra fornecida
    return num if num <= 16384 else "Essa coluna nao existe Tobias!"

input = sys.stdin.read #funcao para ler toda a entrada de uma vez ao inves de precisar especificar linha por linha
data = input().strip().split()

for col in data:
    result = col_to_num(col)
    print(result)
