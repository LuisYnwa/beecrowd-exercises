a, b, c = input().split()
listed = []
a = int(a)
b = int(b)
c = int(c)
listed.append(a)
listed.append(b)
listed.append(c)
listed.sort()
for i in listed:
    print(i)
print()
listed.sort(reverse=True)
for i in listed:
    print(i)