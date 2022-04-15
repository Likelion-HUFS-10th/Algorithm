# 반례
# [3, 30, 31, 34, 5, 9]
# 3과 34(혹은 31)의 비교에서 3이 우선해야 하지만, 해당 로직을 처리하지 못함

# [3, 30, 31, 5, 9]
# 위와 마찬가지

def solution(numbers):
    arr = [str(i) for i in numbers]
    arr.sort(reverse=True)
    answer = ''
    n = len(arr)
    sum_ = 0
    
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            arr[i+1] = arr[i] + arr[i]
        else:
            diff = len(arr[i]) - len(arr[i+1])
            if diff >= 0:
                value = arr[i+1] + ("0" * diff)
                if arr[i] + value > value + arr[i]:
                    answer += arr[i]
                    sum_ += int(arr[i])
                else:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    answer += arr[i]
                    sum_ += int(arr[i])
            else:
                value = arr[i] + ("0" * diff)
                if value + arr[i+1] > arr[i+1] + value:
                    answer += arr[i]
                    sum_ += int(arr[i])
                else:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    answer += arr[i]
                    sum_ += int(arr[i])
                
    sum_ += int(arr[-1])
    answer += arr[-1]
    
    if sum_ == 0:
        return '0'
    else:
        return answer
