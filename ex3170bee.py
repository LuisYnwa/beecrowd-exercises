already_marbles = int(input())
branches = int(input())
tree_needed_marbles = branches // 2
if tree_needed_marbles <= already_marbles:
    print('Amelia tem todas bolinhas!')
else:
    print(f'Faltam {tree_needed_marbles - already_marbles:.0f} bolinha(s)')
