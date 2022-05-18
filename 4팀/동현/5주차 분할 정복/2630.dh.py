"""
분할정복 > 해결할 문제를 여러개의 작은 문제를 분할후, 작은 문제를 해결, 필요시 해결된 해답 모음
함수 안에서 함수를 호출하는 형태 사용 > 재귀..?
첫 색깔과 나머지가 다 같아야 한다는 개념은 파악 > 구현 실패

"""
import sys
n = int(input())
square = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

blue = 0
white = 0

def divide_square(x,y,n):
    global blue, white # 함수 밖의  blue, white 사용
    color = square[x][y] # 첫 색깔
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != square[i][j]: # 첫 색깔과 하나라도 다를 경우 안됨
                divide_square(x, y, n//2)
                divide_square(x, y + n//2, n//2)
                divide_square(x+n//2, y, n//2)
                divide_square(x+n//2, y+n//2, n//2)
                return # 왜 return인지..
    
    if color == 0:
        white += 1
    else:
        blue += 1

divide_square(0,0,n)
print(white)
print(blue)