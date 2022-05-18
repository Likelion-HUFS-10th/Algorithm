n = int(input())
input_stack = [ int(input()) for _ in range(n)]
stack =  []
plus_minus = []
cnt = 1
result_n = True

for i in range (n):
    while input_stack[i] >= cnt:
        stack.append(cnt)
        plus_minus.append("+")
        cnt += 1

    if stack[-1] == input_stack[i]:
        stack.pop()
        plus_minus.append("-")
    else:
        result_n = False


if not result_n:
    print("NO")

else:
    for result in plus_minus:
        print(result)





