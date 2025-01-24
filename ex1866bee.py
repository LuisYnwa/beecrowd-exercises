user_tries = int(input())

for i in range(user_tries):
    odd_or_no = int(input())
    if odd_or_no % 2 == 0:
        print(0)
    else:
        print(1)