a, b, c = map(int, input().split())
while a <= b:
    x = 0
    if c % a == 0:
        x = x + 1
        print(x)
    a = a + 1
 