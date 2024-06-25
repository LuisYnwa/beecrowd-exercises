participants = []

while True:
    age = int(input())
    if age < 0:
        break
    participants.append(age)

average = sum(participants) / len(participants)
print(f'{average:.2f}')