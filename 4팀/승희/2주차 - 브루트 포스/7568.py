"""
x,y 
몸무게, 키
-> x와 y가 모두 크다면 덩치가 큰 것이 맞음.
-> 그러나 둘 중에 하나만 큰 경우에는 같은 등수로 취급됨.
등수는 자신보다 더 큰 덩치의 사람의 수로 정해짐
-> 따라서, 나보다 덩치가 큰 사람의 수를 세고, 
나보다 덩치가 큰 사람의 수와 0명인 사람 간의 차이를 통해서 몇등까지 있는지
알 수 있을 것.
"""

n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

bigger_arr = [0]*n #나보다 덩치 큰 사람이 몇명있는지 저장하기

for i in range(n):
    cnt=0
    for j in range(n):
        if i==j: #비교 대상이 나라면 그냥 넘어가기
            continue
        my_x,my_y = arr[i]
        p_x,p_y = arr[j] #상대방의 몸무게와 키
        if my_x < p_x and my_y<p_y:
            cnt+=1
    bigger_arr[i] = cnt #나보다 덩치 큰 사람의 수를 저장하기

for i in range(n):
    bigger_arr[i] = bigger_arr[i]+1
    print(bigger_arr[i],end=' ')
        