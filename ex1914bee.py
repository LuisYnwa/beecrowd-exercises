#o vencedor eh a soma dos valores para determinar se eh par ou impar
test_cases = int(input())
for i in range(test_cases):
    user1, user1_choice, user2, user2_choice = map(str, input().split())
    user1_number, user2_number = map(int, input().split())
    soma = user1_number + user2_number
    if soma % 2 == 0:
        if user1_choice == "PAR":
            print(user1)
        else:
            print(user2)
    else:
        if user1_choice == "IMPAR":
            print(user1)
        else:
            print(user2)
