a, b, c = input('Insira aqui: ').split()
a = float(a)
b = float(b)
c = float(c)

delta = (b*b) - 4 * a * c
raiz_delta = delta ** 0.5 #calculo da raiz


if a == 0.0 or delta < 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b + raiz_delta) / (2 * a)
    raiz2 = (-b - raiz_delta) / (2 * a)
    
    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')
