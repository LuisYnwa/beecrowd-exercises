import sys

test_cases = int(input())

for _ in range(test_cases):
    radius1, radius2 = map(int, input().split())
    final_radius= radius1 + radius2
    print(final_radius)


