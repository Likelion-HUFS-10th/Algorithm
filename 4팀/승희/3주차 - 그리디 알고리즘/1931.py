"""
n개의 회의에 대하여
회의실을 겹치지 않으면서 최대로 사용할 수 있도록
하나의 회의실에 최대한 여러개의 회의 => 끝나는 시간이 빠른 순
시작시간과 끝나는 시간이 같을 수 있음 + 회의가 끝나는 동시에 다음 회의 시작 가능
=> 시작 시간이 빠른 순
"""

n = int(input()) #회의가 몇개인지
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

start = arr[0][0]
end = arr[0][1]
cnt=1

for i in range(1,n):
    start_next,end_next = arr[i]
    if start_next>=end:
        start = start_next
        end = end_next
        cnt+=1

print(cnt)
