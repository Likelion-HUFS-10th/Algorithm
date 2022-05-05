n = int(input())

def solution(k):
    if k == 0 or k == 1:
        return k
    return solution(k-1) + solution(k-2)

print(solution(n))