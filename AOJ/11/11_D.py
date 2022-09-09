class Dice:
    def __init__(self, array):
        self.top = array[0]
        self.flo = array[1]
        self.rig = array[2]
        self.lef = array[3]
        self.dow = array[4]
        self.btm = array[5]

    def up(self):
        self.top, self.flo, self.btm, self.dow = self.flo, self.btm, self.dow, self.top

    def down(self):
        self.top, self.flo, self.btm, self.dow = self.dow, self.top, self.flo, self.btm

    def right(self):
        self.rig, self.flo, self.lef, self.dow = self.dow, self.rig, self.flo, self.lef

    def left(self):
        self.rig, self.flo, self.lef, self.dow = self.flo, self.lef, self.dow, self.rig

    def spin_left(self):
        self.top, self.lef, self.btm, self.rig = self.rig, self.top, self.lef, self.btm

    def spin_right(self):
        self.top, self.lef, self.btm, self.rig = self.lef, self.btm, self.rig, self.top

    def is_same_setting(self, ary):
        if (
            self.top == ary[0]
            and self.flo == ary[1]
            and self.rig == ary[2]
            and self.lef == ary[3]
            and self.dow == ary[4]
            and self.btm == ary[5]
        ):
            return True

    def is_same_dice(self, array):
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.is_same_setting(array) is True:
                        is_same = True
                    self.right()
                self.up()
            self.right()
            self.down()
        return is_same


# n個のサイコロを作る


n = int(input())

surfaces_stack = [None] * n
for i in range(n):
    surfaces_stack[i] = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(i + 1, n):
        dice = Dice(surfaces_stack[i])
        if dice.is_same_dice(surfaces_stack[j]):
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")
