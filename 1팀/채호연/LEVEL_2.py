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

#2884 : 
