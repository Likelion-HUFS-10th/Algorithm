import sys
input = sys.stdin.readline

def possible(m):
    result = 'Yes'
    for _ in range(m):
        k_num = int(input())    
        k = list(map(int, input().split()))
        for i in range(k_num-1):
            if k[i] < k[i+1]:
                result = 'No'
    return result

n, m = map(int, input().split())
print(possible(m))