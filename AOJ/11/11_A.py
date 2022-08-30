"""
①入ってきた数字を割り当てる
②指示された方向によってさいころを転がす関数を適応させる
③上面の数字を表示させる
"""
dice_number = list(map(int, input().split()))
direction = list(input())


def init_dice():
    return {
        "front": dice_number[0], "back": dice_number[5],
        "up": dice_number[4], "right": dice_number[2], "down": dice_number[1], "left": dice_number[3]
    }


def up(dice):
    f, u, d, b = [dice["front"], dice["up"], dice["down"], dice["back"]]
    dice["front"] = d
    dice["up"] = f
    dice["down"] = b
    dice["back"] = u
    return dice


def down(dice):
    f, u, d, b = [dice["front"], dice["up"], dice["down"], dice["back"]]
    dice["front"] = u
    dice["up"] = b
    dice["down"] = f
    dice["back"] = d
    return dice


def left(dice):
    f, l, r, b = [dice["front"], dice["left"], dice["right"], dice["back"]]
    dice["front"] = r
    dice["left"] = f
    dice["right"] = b
    dice["back"] = l
    return dice


def right(dice):
    f, l, r, b = [dice["front"], dice["left"], dice["right"], dice["back"]]
    dice["front"] = l
    dice["left"] = b
    dice["right"] = f
    dice["back"] = r
    return dice


def show(dice):
    print(dice["front"])


dice = init_dice()

for direction_char in direction:
    if direction_char == "N":
        dice = up(dice)
    if direction_char == "S":
        dice = down(dice)
    if direction_char == "W":
        dice = left(dice)
    if direction_char == "E":
        dice = right(dice)
show(dice)
