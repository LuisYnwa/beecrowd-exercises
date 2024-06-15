n = int(input())
interval = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
in_ = out_ = 0
if n < 10000:
    for i in range(n):
        x = int(input())
        if x in interval:
            in_ += 1
        else:
            out_ +=  1
else:
    print('ERROR')

print(f'{in_} in')
print(f'{out_} out')

