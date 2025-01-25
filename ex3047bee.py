#soma das 3 criancas tem que dar a idade inicial da monica
#printar a idade da 3 crianca n especificada
idade_monica = int(input())
filhos = []
for i in range(2):
    idade_crianca = int(input())
    filhos.append(idade_crianca)
    idade_monica -= idade_crianca

filhos.append(idade_monica)
print(max(filhos))
