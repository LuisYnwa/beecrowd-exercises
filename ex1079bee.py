chances = int(input())
for i in range (chances):
    x, y, z = map(float, input().split()) #pega a linha de entrada do usuário e a divide em uma lista de strings. Então, map(float, ...) aplica a função float a cada elemento dessa lista, convertendo-os em números de ponto flutuante. Finalmente, x, y, z = ... atribui esses valores flutuantes às variáveis x, y e z.
    result1 = x * 2
    result2 = y * 3
    result3 = z * 5
    final_result = (result1 + result2 + result3) / (2 + 3 + 5)
    print(f'{final_result:.1f}')