while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x > y:
        x, y = y, x
        print(f"{x} {y}")
    else:
        print(f"{x} {y}")
