import sys
n=int(sys.stdin.readline())

freq = [0] * 10001            # 만개의 데이터 담을 배열 선언

for i in range (n):
    num= int(input())          
    freq[num] += 1            # 값을 입력받을 때마다 +1 해주기


for i in range(10001):        # 전체를 돌면서 0이 아닌 경우 출력하기
    if freq[i] !=0:
        for j in range(freq[i]):  
            print(i)
