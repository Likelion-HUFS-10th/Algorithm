n = int(input())

cnt = 1
result = 1
while 1:
    if n == 1:
        back = 0    
    if result < n:
        cnt += 1
        back = result
        result += cnt
    else:
        break
number = n - back
momson = cnt + 1
if cnt % 2 == 1:
    print(f"{momson - number}/{number}")
else:
    print(f"{number}/{momson - number}")