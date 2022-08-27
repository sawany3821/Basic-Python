class Dice:
    def __init__(self, array):
        self.t = array[0] 
        self.f = array[1] 
        self.r = array[2]
        self.l = array[3]
        self.d = array[4]
        self.b = array[5]

    def up(self):#上に転がる
        self.t, self.f, self.b, self.d = self.f, self.b, self.d, self.t

    def down(self):#下に転がる
        self.t, self.f, self.b, self.d = self.d, self.t, self.f, self.b

    def right(self): #右に転がる
        self.r, self.f, self.l, self.d = self.d, self.r, self.f, self.l

    def left(self): #左に転がる
        self.r, self.f, self.l, self.d = self.f, self.l, self.d, self.r
        
    def spin_left(self):#左回転
        self.t, self.l, self.b, self.r = self.r, self.t, self.l, self.b
    
    def spin_right(self):#右回転
        self.t, self.l, self.b, self.r = self.l, self.b, self.r, self.t

    def is_same_setting(self, array): #dice1 == dice2かどうか判定する
        if self.t == array[0] and self.f == array[1] and self.r == array[2] and \
        self.l == array[3] and self.d == array[4] and self.b == array[5]:
            return True
    
    def is_same_dice(self, array): #24通りあるダイスの中にdice2があるかどうか
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.is_same_setting(array) == True:
                        is_same = True
                    self.right()
                self.up()
            self.right()
            self.down()
        return is_same

#n個のサイコロを作る
n = int(input())
surfaces_stack = [None] * n
for i in range(n):
    surfaces_stack[i] = list(map(int,input().split()))

#サイコロが一緒かどうか判定する
for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(surfaces_stack[i])
        if dice.is_same_dice(surfaces_stack[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')