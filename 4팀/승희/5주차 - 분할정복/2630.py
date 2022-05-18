"""
색종이를 잘라서 확인해야 하기에 => 재귀겠구나! 어차피 범위는 //2로 똑같기 때문에\
    같은 형태가 반복된다는 생각
"""
import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
blue,white = 0,0

#시작점만 잡아보기
def cut_paper(x,y,n):
    global blue,white
    num = arr[x][y]
    flag = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=arr[i][j]:
                flag = False
                break
        if not flag:
            break
    #다르다는 뜻
    if not flag:
        cut_paper(x,y,n//2)
        cut_paper(x,y+n//2,n//2)
        cut_paper(x+n//2,y,n//2)
        cut_paper(x+n//2,y+n//2,n//2)
        return
    else:
        if num==1:
            blue+=1
        else:
            white+=1
        return

cut_paper(0,0,n)
print(white)
print(blue)

"""
틀린 코드
def cut_paper(arr,start_x,end_x,start_y,end_y):
    global blue,white
    if start_x+1 >= end_x or start_y+1 >= end_y or end_x - start_x != end_y - start_y:
        return #범위를 벗어남
    flag = True
    num = arr[start_x][start_y]
    for i in range(start_x,end_x):
        for j in range(start_y,end_y):
            if num!=arr[i][j]:
                flag=False
                break
        if not flag:
            break

    if not flag:
        cut_paper(arr,start_x,end_x//2,start_y,end_y//2)
        cut_paper(arr,start_x,end_x//2,end_y//2,end_y)
        cut_paper(arr,end_x//2,end_x,end_y//2,end_y)
        cut_paper(arr,end_x//2,end_x,start_y,end_y//2)
        return
    else:
        if num==1:
            blue+=1
        else:
            white+=1
        return"""

