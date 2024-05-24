line1 = input().split(" ")
line2 = input().split(" ")
code, amount, price = line1
code2, amount2, price2 = line2
total = int(amount) * float(price) + int(amount2) * float(price2)
print(f'Final price: {total}')
