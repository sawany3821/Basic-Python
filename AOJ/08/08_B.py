while True:
    a = input()
    if a == "0":
        break
    else:
        a = list(a)
        b = map(int, a)
        print(sum(b))
