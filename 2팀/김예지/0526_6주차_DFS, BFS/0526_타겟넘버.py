from collections import deque
def solution(numbers, target):
    answer = 0
    deq = deque()
    deq.append(0)
    for number in numbers:
        for _ in range(len(deq)):
            v = deq.popleft()
            deq.append((v+number))
            deq.append((v-number))
    answer = deq.count(target)
    return answer

# print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))