import math
#aceita ai meu pr

x1 = float(input().split())
x2 = float(input().split())
y1 = float(input().split())
y2 = float(input().split())

#Realiza os calculos#

calx = (x2 - x1) * (x2 - x1)
caly = (y2 - y1) * (y2 - y1)

distancia = (calx + caly) ** 0.5

print("{0:.4f}".format(distancia))