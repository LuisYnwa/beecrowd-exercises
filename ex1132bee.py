x = int(input())
y = int(input())
sum = 0
if x % 13 != 0:
    sum += x
if y % 13 != 0:
    sum += y
    
for i in range(x+1, y):
    if i % 13 != 0:
        sum += i
    else:
        continue
print(sum)
