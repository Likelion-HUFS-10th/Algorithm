'''

색종이

저는 어려웠습니다..
구글링 해서 도움 받았습니다...
완벽이해 x

'''
import sys

input = sys.stdin.readline

n = int(input())

paper = [ list(map(int,input().split()) for _ in range(n)) ]

white, blue = 0, 0

def cut_paper(x,y,n):
    global white, blue
    paint = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != paint:
                cut_paper(x, y, n//2)
                cut_paper(x+n//2, y, n//2)
                cut_paper(x, y+n//2, n//2)
                cut_paper(x+n//2, y+n//2, n//2)
                return
    if paint == 0:
        white += 1
    else:
        blue += 1

cut_paper(0,0,n)
print(white)
print(blue)

