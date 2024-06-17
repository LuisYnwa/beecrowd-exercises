in_order = []
for i in range(1, 101):
    number = int(input())
    in_order.append(number)
greatest_value = max(in_order) # funcao para achar o maior valor presente em uma lista sem a necessidade de organiza-la
print(greatest_value)
greatest_position = in_order.index(greatest_value) + 1 # 1 mais para contar a posicao sem ser na visao da maquina, ou seja, a partir do 1
print(greatest_position)