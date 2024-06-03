#tabela: 
# 1	Cachorro Quente	R$ 4.00
# 2	X-Salada	R$ 4.50
# 3	X-Bacon	R$ 5.00
# 4	Torrada Simples	R$ 2.00
# 5	Refrigerante	R$ 1.50
x, y = input().split()
x = int(x) #x representa o codigo e y representa a quantidade de itens
#if x or y == 0:
    #print('selecione pelo menos um item dos codigos, indo de 1 a 5')

if x == 1:
    preco = float(y) * 4.00
    print(f'Total: R$ {preco}')
elif x == 2:
    preco = float(y) * 4.50
    print(f'Total: R$ {preco}')
elif x == 3:
    preco = float(y) * 5.00
    print(f'Total: R$ {preco}')
elif x == 4:
    preco = float(y) * 2.00
    print(f'Total: R$ {preco}')
elif x == 5:
    preco = float(y) * 1.50
    print(f'Total: R$ {preco}')