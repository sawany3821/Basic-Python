i = int(input())
ch, rank = list(map(str, input().split()))
rank = int(rank)
cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]
cards[pattern.index(ch)][rank-1] = True
if cards[i][j] == False:
    print(pattern[i], j+1)