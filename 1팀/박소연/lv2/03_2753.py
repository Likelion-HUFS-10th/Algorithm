# 윤년이면 1, 아니면 0
# 윤년 = 4의배수 and 100의배수X or 400의 배수

year = int(input())

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(1)
else:
  print(0)