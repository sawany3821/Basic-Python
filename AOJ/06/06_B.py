S = [i for i in range(1, 14)]
H = [i for i in range(1, 14)]
C = [i for i in range(1, 14)]
D = [i for i in range(1, 14)]

sum_card = int(input())

for x in range(sum_card):
    mark, i = list(map(str, input().split()))
    i = int(i)
    if mark == "S":
        S.remove(i)
    if mark == "H":
        H.remove(i)
    if mark == "C":
        C.remove(i)
    if mark == "D":
        D.remove(i)

for output in S:
    print("S", output)
for output in H:
    print("H", output)
for output in C:
    print("C", output)
for output in D:
    print("D", output)
