import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    heap = []
    for i in food_times:
        heapq.heappush(heap, (food_times[i], i+1))
    previous = 0
    food_num = len(food_times)

    while heap:
        t = (heap[0][0] - previous) * food_num
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(heap)
            food_num -= 1
        else:
            idx = k % food_num
            heap.sort(key=lambda x:x[1])
            answer = heap[idx][1]
            break
    return answer
food_times = [4, 1, 1, 2, 5]
k = 10
print(solution(food_times, k))