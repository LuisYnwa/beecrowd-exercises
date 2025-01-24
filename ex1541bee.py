import math

while True:
    nums_user = list(map(int, input().split()))
    if 0 in nums_user:
        break
    else:
        num_user1, num_user2, num_user3 = nums_user
        square_meters = num_user1 * num_user2
        allowed_area = square_meters / (num_user3 / 100) #divisão por 100 para se adaptar á qualquer % enviada pelo usuário
        land_side = int(math.sqrt(allowed_area)) # Momento em que o resultado é truncado
        print(land_side)