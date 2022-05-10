n = int(input())
vpss = [
    input()
    for _ in range(n)
]

def find_vps(vps):
    stack = [] #스택 생성
    for i in range(len(vps)):
        if vps[i]=="(": #왼쪽 괄호인 경우에는 푸쉬
            stack.append("(")
        elif vps[i]==")":
            if len(stack)>=1 and stack[-1]=="(":
                stack.pop()
            else:
                return "NO"
    if stack:
        return "NO" #남아있으면 안됨
    else:
        return "YES"

for vps in vpss:
    print(find_vps(vps))