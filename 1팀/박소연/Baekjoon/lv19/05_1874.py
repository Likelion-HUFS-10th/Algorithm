# 스택 수열
# [1,2,3,4] [+,+,+,+]
# 4,3 [1,2] [-,-]  [4,3]
# 6 [1,2,5,6] [+,+]
# [1,2,5] [-] [4,3,6]
# 8,7 [1,2,5,7,8] [+,+]
# 5,2,1 [] [-,-,-,-,-] [4,3,6,8,7,5,2,1]
# 첫번째 수보다 작은 수를 stack에 오름차순으로 추가 -> stack의 top과 같으면 pop 다르면 no 종료

stack, answer = [], []
cur, flag = 1, True

n = int(input())
for _ in range(n):
  input_num = int(input())
  while cur <= input_num:
    # input_num까지 오름차순으로 stack에 push
    stack.append(cur)
    answer.append("+")
    cur += 1
    # stack의 top이랑 input_num이 같으면 pop
  if stack[-1] == input_num:
    stack.pop()
    answer.append("-")
  # 다르다 = input_num이 top보다 작다 = 밑에 깔려 있어서 못 뺀다
  else:
    flag = False
    break
if flag == False:
  print("NO")
else:
  for elem in answer:
    print(elem)
