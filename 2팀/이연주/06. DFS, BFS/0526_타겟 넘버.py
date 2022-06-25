def solution(numbers, target):
    answer = 0
    queue = [[numbers[0], 0], [-1*numbers[0], 0]]
    n = len(numbers)
    while queue:
        temp, index = queue.pop()
        index += 1
        if index < n:
            queue.append([temp+numbers[index], index])
            queue.append([temp-numbers[index], index])
        else:
            if temp == target:
                answer += 1
    return answer