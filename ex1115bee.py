while True:
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        print(f"primeiro")
    elif x < 0 and y > 0:
        print(f"segundo")
    elif x < 0 and y < 0:
        print(f"terceiro")
    elif x > 0 and y < 0:
        print(f"quarto")
    elif x == 0 and y == 0:
        break