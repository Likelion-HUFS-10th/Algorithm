#2739 : 구구단 N단 출력하기(1N ~ 9N까지) : boolean-condition 이 아닌 iterable. 따라서 for를 사용한다.
N = int(input())
for i in range(1, 10):
    print("{} * {} = {}" .format(N, i, N * i))

#10950 : 반복 횟수 T 입력 받은 후 주어진 수를 입력받아 출력하는 행위를 T번 반복하도록 하는 프로그램 작성. 이번엔 while 로.
T = int(input())
count = 0
while count < T:
    A, B = map(int, input().split())
    print(A + B)
    count += 1

#8393 : 등차 1인 등차수열 제1항~n항 합. 누적합계이므로 Accumulator가 필요하다.
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#15552번 : 빠른 A+B 출력
'''
input() VS sys.stdin.readline()
 1) propmt의 출력여부 : input()은 prompt에 입력값을 한 번 출력하기 때문에 sys.stdin.readline()보다 느림
  2) sys.stdin.readline()은 한 번에 읽어서 버퍼에 저장 
     input()은 값을 입력할 때마다 버퍼에 저장
'''
import sys #sys.stdin.readline() 사용 위해 import 필요
T = int(input())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split()) #map() 내에서 int() 사용하기 때문에 .rstrip()통한 개행문자 제거 불필요
    print(A + B)

#2741 : N 찍기
N = int(input())
for i in range(1, N+1):
    print(i)

#2742 : 기찍 N : 반대순서로 찍기
N = int(input())
N_lst = []
for i in range(1, N+1):
    N_lst.append(i)
N_lst.reverse()
for i in N_lst:
    print(i)

#11021 : A+B - 7탄 : Case #1: T!!
T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #{}: {}" .format(i, A + B))

#11022 : Beautiful A+B : Case #n: A + B = A + B !!
T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}" .format(i, A, B, A + B))