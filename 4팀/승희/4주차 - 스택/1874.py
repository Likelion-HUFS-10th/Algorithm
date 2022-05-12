"""
num 은 다음으로 push 될 숫자를 의미
target_num 은 지금 출력해야하는 숫자를 의미
NO 인지 아닌지 구분해서 + - 를 출력해야 하므로 배열에 담아 출력
불가능한 경우라고 생각한 케이스
=>target_num 이 num보다 크다면 그냥 num에 숫자를 더해서 append를 계속 해주면 됨
=> 문제는 target_num 이 num보다 작은 경우에 stack의 top이 내가 출력해야 하는 숫자가 아닐때
    => 더 이상 볼 필요가 없으므로 NO를 반환
"""

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

stack = []

# num은 다음 더해질 숫자
def stack_arr(arr,num=1):
    result_arr =[]
    for i in range(len(arr)):
        target_num = arr[i]
        if target_num >= num:
            for _ in range(target_num-num+1):
                stack.append(num)
                result_arr.append("+")
                num+=1
            stack.pop()
            result_arr.append("-")
        elif target_num < num:
            if stack[-1]==target_num:
                result_arr.append("-")
                stack.pop()
            else:
                return "NO"
    return result_arr

result_arr = stack_arr(arr)
if type(result_arr)==str:
    print(result_arr)
else:
    for i in range(len(result_arr)):
        print(result_arr[i])