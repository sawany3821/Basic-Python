while True:
    a, op, b = map(str, input().split())
    if op == "?":
        break
    a = int(a)
    b = int(b)
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)
