# 일일 온도
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지
# 인덱스를 stack에 저장

input_t = [73, 74, 75, 71, 69, 72, 76, 73]
stack, result = [], [0] * len(input_t)

for i in range(len(input_t)):
  # stack에는 작은 값의 인덱스만 들어감
  # 현재 온도가 stack의 top을 인덱스로 가지는 온도보다 크면 = 인덱스 차이(며칠 기다려야 하는지) 계산
  while stack and input_t[i] > input_t[stack[-1]]:
    small_index = stack.pop()
    result[small_index] = i - small_index
  stack.append(i)
print(result)
