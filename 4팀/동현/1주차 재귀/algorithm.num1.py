
while True: # 올바른 입력에 대해서만 진행될 수 있게 while 반복문 사용
    N = int(input('정수 N을 입력하시오: '))
    if N >= 0 and N <= 12:
        num = 1
        result = 1
        while num <= N: # 'N'까지 반복하기 위한 while 반복문 사용
            result = result * num
            num += 1
        print(result)
        break
    else:
        print('잘못된 입력입니다.')
        continue # 잘못된 입력에 대한 재입력 by while 반복문





