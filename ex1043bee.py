a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a + b > c and b + c > a and a + c > b:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro}')
else:
    area_trapezio = ((a + b) * c) / 2
    print(f'Area = {area_trapezio}')