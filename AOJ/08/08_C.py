import collections
from collections import Counter
import sys


l = sys.stdin.readlines()
l2 = [line.strip("\n").replace(" ", "").replace(".", "").lower() for line in l]
l2 = "".join(l2)

a = list(map(chr, range(97, 123)))
b = list([0]*26)
c = dict(zip(a, b))
d = dict(collections.Counter(l2))

for d_key, d_value in d.items():
    if d_key in a:
        e = {d_key:d_value}
        c.update(e)

for c_key, c_value in c.items():
    print(f"{c_key} : {c_value}")
