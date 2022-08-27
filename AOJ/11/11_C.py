"""
手順
①2つのダイスを作る
②1つ目のダイスは固定させて、2つ目のダイヤを走査する
③走査は（1と6固定で4通り）、（2と5固定で4通り）、（3と4固定で4通り）ある。逆もあるので3*4*2 = 24 通り
④24通りあるなかでその中に含まれていたらprint("Yes")入っていなかった場合print("No")
"""

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

dice1 = list(map(int,input().split()))
dice2 = list(map(int,input().split()))

dice1 = Dice(dice1)

if dice1.is_same_dice(dice2) == True: #24通りにあればTrueでYesをプリントする
    print('Yes')
else:
    print('No')
