sum_card = int(input())

for x in range(sum_card):
    mark, i = list(map(str, input().split()))

i = int(i)
limit = range(1, 14)
mark_set = ["S", "H", "C", "D"]

if mark == "S" and i in limit:
    for y in limit:
        if y != i:
            print("S", y)

if mark not in "S" or mark not in "H" or mark not in "C" or mark not in "D":
    for z in limit:
        if mark not in "S":
            print(f"S {z}")
    for z in limit:
        if mark not in "H":
            print(f"H {z}")
    for z in limit:
        if mark not in "C":
            print(f"C {z}")
    for z in limit:
        if mark not in "D":
            print(f"D {z}")
