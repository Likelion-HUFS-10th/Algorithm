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

################################# 통과 ########################################

