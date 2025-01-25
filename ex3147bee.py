H, E, A, O, W, X = map(int, input().split())
bem = H, E, A,
mal = W, O

total_bem = sum(bem)
total_mal = sum(mal)

if total_bem > total_mal:
    print('Middle-earth is safe.')

elif total_bem + X > total_mal:
    print('Middle-earth is safe.')

else:
    print('Sauron has returned.')

