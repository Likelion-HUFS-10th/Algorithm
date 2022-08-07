# 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# Ai보다 크면 stack에 뒤에서부터 push -> top을 pop

################################# 시간초과 - 결국엔 이중for문 ########################################
# num = int(input())
# input_num = list(map(int, input().split()))
# stack, answer = [], []

# for i in range(len(input_num)):
#   stack, cnt = [], i + 1
#   a_i = input_num[i]
#   while cnt < len(input_num):
#     if input_num[cnt] > a_i:
#       stack.append(input_num[cnt])
#     cnt += 1
#   if stack and i != len(input_num) - 1:
#     answer.append(stack[0])
#   elif stack and i == len(input_num) - 1:
#     answer.append(-1)
#   else:
#     answer.append(-1)

# for elem in answer:
#   print(elem, end=" ")

################################# 얘도... -> O(n^2) ########################################
# outstack: 결과 list
# okenstack: 비교용 stack

# num = int(input())
# outstack = []
# input_list = list(map(int, input().split()))

# while input_list:
#   input_pop = input_list.pop(0)
#   okenstack = [input_list[i] for i in range(len(input_list)-1, -1, -1)]
#   while okenstack:
#     if okenstack[-1] > input_pop:
#       outstack.append(okenstack[-1])
#       break
#     else:
#       okenstack.pop()
#       if not okenstack:
#         outstack.append(-1)
# if not okenstack:
#   outstack.append(-1)


# for elem in outstack:
#   print(elem, end=" ")

################################# 통과 ########################################
# stack: 원소의 인덱스 넣기
# 디버깅 해보기

num = int(input())
input_list = list(map(int, input().split()))
result, stack = [-1] * num, [0]

for i in range(1, num):
  while stack and input_list[stack[-1]] < input_list[i]:
    result[stack.pop()] = input_list[i] # 오큰수 나오면 stack에서 인덱스 pop -> not stack이 되니까 while문 종료
  stack.append(i) # 다음 비교를 위해 stack에 인덱스 append

for elem in result:
  print(elem, end=" ")
