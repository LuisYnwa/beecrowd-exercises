#WRONG ANSWER(15%)  
def build_array(n):
    array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = min(i, j, n-i-1, n-j-1) + 1
    return array

def print_array(array):
    for row in array:
        print(" ".join(f"{val:>3}" for val in row).rstrip())
    print()

while True:
    num = int(input().strip())
    if num == 0:
        break
    else:
        result_array = build_array(num)
        print_array(result_array)
