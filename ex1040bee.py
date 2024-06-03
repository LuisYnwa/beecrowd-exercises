a, b, c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media_ponderada = (a * 2) + (b * 3) + (c * 4) + (d * 1) 
media = media_ponderada / 10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame_nota = float(input())
    print(f'Nota do exame: {exame_nota:.1f}')
    nota_final = (exame_nota + media) / 2

    if nota_final >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {nota_final:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {nota_final:.1f}')