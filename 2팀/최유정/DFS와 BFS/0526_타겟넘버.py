import sys
input = sys.stdin.readline
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append(0)
    for num in numbers:
        for _ in range(len(queue)):
            result = queue.popleft()
            queue.append(result + num)
            queue.append(result - num)
    for i in queue:
        if i == target:
            answer += 1
    return answer

numbers = list(map(int, input().split()))
target = int(input())
print(solution(numbers, target))