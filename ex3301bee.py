while True:
    try:
        nephews = list(map(int, input().split()))
        # verifica qual das idades é a do meio
        middle_age = sorted(nephews)[1] #sempre deixa em ordem para o nome corresponder a idade citada
        
        if middle_age == nephews[0]:
            print('huguinho')
        elif middle_age == nephews[1]:
            print('zezinho')
        elif middle_age == nephews[2]:
            print('luisinho')
    except EOFError:
        break
