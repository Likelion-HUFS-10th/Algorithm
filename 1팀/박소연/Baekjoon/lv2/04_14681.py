# 좌표 알아내기
# x, y좌표 0과 비교 -> 논리연산자

x = int(input())
y = int(input())

if x>0 and y>0: print(1)
elif x<0 and y>0: print(2)
elif x<0 and y<0: print(3)
else: print(4)