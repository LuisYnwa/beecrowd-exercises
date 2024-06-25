#n1, n2 = map(int, input().split())
n1, n2 = map(int, input().split())
while n1 <= 0 or n2 <= 0:
    if n1 <= 0:
        n1 = int(input())
    else:
        n2 = int(input())
print(n1 + n2)
