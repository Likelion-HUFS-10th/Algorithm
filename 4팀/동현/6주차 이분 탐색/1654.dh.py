"""
절반으로 짜르는 방식으로 접근..??
함수로 접근해봤지만 오류 발생 > 반드시 함수 사용x
while로 다시 접근
"""

import sys
sys.setrecursionlimit(10**7)

K,N = map(int, sys.stdin.readline().split())

line_list = []
for _ in range(K):
    line_list.append(int(input()))
     
line_list.sort(reverse = True)
start = 1
end = line_list[0]

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in line_list:
        count += i // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)


#def find_num(array, start, end):
    #mid = (start + end) // 2
    #count = 0
    #max = mid
    #for i in array:
        #count += i // mid
    
    #if count >= N:
        #find_num(array, mid+1, end)
    #else:
        #find_num(array,start, mid-1)
    #return max

#print(find_num(line_list,start,end))