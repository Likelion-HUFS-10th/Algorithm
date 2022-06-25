# 11654번 : 아스키코드 출력
'''
ord : unicode 반환 함수이나, 1~127까지는 아스키코드와 동일해서 사용 가능하다고 함.
'''
c = input()
print(ord(c))

#11720 : 숫자의 합
length = int(input())
number = list(map(int, input()))
sum = 0
for i in range(len(number)):
    sum += number[i]
print(sum)

#10809 : 알파벳 찾기 : 미결


