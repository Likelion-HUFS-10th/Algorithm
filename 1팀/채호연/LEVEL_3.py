#2739 : 구구단 N단 출력하기(1N ~ 9N까지) : boolean-condition 이 아닌 iterable. 따라서 for를 사용한다.
N = int(input())
for i in range(1, 10):
    print("{} * {} = {}" .format(N, i, N * i))

#10950 : 반복 횟수 T 입력 받은 후 주어진 수를 입력받아 출력하는 행위를 T번 반복하도록 하는 프로그램 작성. 이번엔 while 로.
T = int(input())
count = 0
while count < T: #while의 경우 'count +=' 연산을 어떤 줄에 할당하는 지가 중요하다! 위치를 반복문 내의 펑션 보다 앞으로 잡으면 카운트가 차버려 펑션이 시행이 되지 않는다!
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
from curses import A_NORMAL
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

#2438 : 별찍기
N = int(input())
for i in range(1, N+1):
    print('*' * i )

#2439 : 오른쪽에서부터 별 찍기
N = int(input())
for i in range(1, N+1):
    print(('*' * i).rjust(N, " ")) #.rjust()을 이용해 우정렬 후 빈칸 공백으로 채우기
'''
.rjust(width=int, fillchar=string)
'''

#10871 : X 보다 작은수
N, X = map(int, input().split())
N_lst = list(map(int, input().split()))
X_str = ""
for i in range(0, len(N_lst)):
    if N_lst[i] < X:
        X_str += (str(N_lst[i]) + " ")
print(X_str)
'''
까다로웠던 포인트
1. 두 번 째줄에 한 번에 수열 N을 입력받는 방식. : 리스트로 해결
2. N_lst[i]의 출력값을 띄어쓰기로 구분 된 string으로 출력하는 것 :
    N_lst[i] == integer. 따라서 String Concatenation을 위해선 str()으로 처리해줄 필요가 있다.
'''

#10952 : A + B -5 / 입력값이 0, 0일 때 반복 중단. => While loop under Boolean condition.
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)

#10951 : 입력이 끝날 때까지 A + B 출력 => 무한루프?
'''
당연히 무한 루프가 아니었다.
아무 것도 입력되지 않는다 = time을 설정해 입력이 되지 않는 상태가 timeout 기준을 초과하면 exit 되는 것으로 생각했으니 그게 아니었다.
아무 것도 입력되지 않는다 = 아무 것도 입력하지 않은 채 엔터를 쳤다.
당연히 이 경우 Value Error 가 출력된다. 이를 EOF(End Of File)이라고 한다. 읽어들일 것이 더 이상 없다는 뜻.
그래서 이 Value Error를 예외 처리해서 프로그램이 정상 종료되도록 해야한다.
'''
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break

#1110 : 더하기 싸이클 - 원래 수로 돌아올 때까지 연산을 반복하는 문제 / N = 정수
'''
if 먼저 주어진 수가 10보다 작다면
    앞에 0을 붙여 두 자리 수로 만들고, 
각 자리의 숫자를 더한다. => 앞에서 구한 합

그 다음, "주어진 수의 가장 오른쪽 자리 수"와 "앞에서 구한 합의 가장 오른쪽 자리 수"를 이어 붙이면 "새로운 수"를 만들 수 있다.

if 결과 == N:
    싸이클 출력
    break

이때 싸이클의 길이 = 반복 횟수를 출력해야하므로, accumulator(counter) 필요
'''
N = int(input())
cnt = 0
p_before = 0

while True:
    if int(N) < 10:
        N_sum = int(N)
    else:
        N_sum = 
   
    p_before = p_before + N_sum
    cnt += 1

    if p_before == N:
        print(cnt)
        break
    
     N = "0" + str(N)[1]
