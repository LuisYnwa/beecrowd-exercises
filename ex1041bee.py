#Se x e y forem ambos iguais a zero, o ponto está na origem.
#Se x for igual a zero, o ponto está no eixo Y.
#Se y for igual a zero, o ponto está no eixo X.
#Se x e y forem positivos, o ponto está no primeiro quadrante (Q1).
#Se x for negativo e y for positivo, o ponto está no segundo quadrante (Q2).
#Se x e y forem negativos, o ponto está no terceiro quadrante (Q3).
#Caso contrário, o ponto está no quarto quadrante (Q4).
x, y = input().split()
x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
else:
    print('Q4')