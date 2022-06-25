#1330 : 두 수 입력 받아 비교하기. 조건문으로 분기하여 결과 출력. 포인트는 '=='. 관계 비교이기 때문에 =가 아니라는 것 항상 유의.
from tkinter import Y


A, B = map(int, input().split())
if A > B :
    print('>')
elif A == B:
    print('==')
else:
    print('<')

#9498 : 시험점수를 성적으로 변경하기.
grade = int(input())
if grade >= 90 and grade <= 100:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

#2753 : 윤년 판별하기 / 조건 : (4의 배수 & 100의 배수가 아님) OR 400의 배수 일 경우 윤년. / 포인트는 연산자 사이의 우선순위를 파악하고 있는가...?
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('1')
else:
    print('0')

#14681 : 좌표 P(x, y)의 x/y값 입력 받고 사분면(Quadrant) 판별하기
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x > 0 and y < 0:
    print('4')
elif x < 0 and y > 0:
    print('2')
else:
    print('3')

#2884 : 45분 이른 알람 설정하기
'''
해결의 포인트는 시간은 00시, 분 < 45 인 경우 출력을 H 대신 23이 되도록 처리하는 것이었다.
'''
H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else:
    if H == 0:
        print(23, M+15)
    else:
        print(H-1, M+15)

#2525번 : 오븐 시계 / 요리 완료 시간이 24시간을 넘었을 때의 조건을 구현하는 부분이 까다로웠다.
H, M = map(int, input().split())
cook_total = int(input())
cook_hour = cook_total // 60
cook_min = cook_total % 60
if M + cook_min > 60:
    if H + cook_hour + 1 >= 24:
        print(H + cook_hour -23, M + cook_min - 60)
    else:
        print(H + cook_hour + 1, M + cook_min - 60)
elif M + cook_min == 60:
    if H + cook_hour + 1 >= 24:
        print(H + cook_hour - 23, 0)
    else:
        print(H + cook_hour + 1, 0)
else:
    if H + cook_hour >= 24:
        print(H + cook_hour - 24, M + cook_min)
    else:
        print(H + cook_hour, M + cook_min)

#2480번 : 주사위 세 개.
d1, d2, d3 = map(int, input().split())
if d1 == d2 == d3:
    print(10000 + d1 * 1000)
else:
    if d1 == d2:
        print(1000 + d1 * 100)
    elif d2 == d3:
        print(1000 + d2 * 100)
    elif d3 == d1:
        print(1000 + d3 * 100)
    else:
        d_list = [d1, d2, d3]
        print(int(max(d_list)) * 100)

'''
LEVEL_2 CLEAR
'''
