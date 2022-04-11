n = int(input('몇번째 피보니치수를 구할까요?: '))
lista = [0,1] # 리스트 끝에 두가지 요소들을 더해주는 방식을 사용
if n <= 20 and n > 1:
    for i in range(1,n):
        lista.append(int(lista[-2]) + int(lista[-1])) # for 반복문을 통해 리스트에 피보나치수를 추가해주는 방식 사용
    print(lista[-1])
elif n == 0: # 빈리스트로 시작하는 방법에 대한 해결법을 찾지못해 0,1의 경우는 따로 케이스를 나눔
    print('0')
elif n == 1:
    print('1')
else:
    print('잘못된 입력입니다.')

