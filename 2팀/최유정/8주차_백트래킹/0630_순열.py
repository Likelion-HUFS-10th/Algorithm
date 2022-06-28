import sys
input = sys.stdin.readline
import math

def back():
    global cnt
    if len(ans) == len(case):
        cnt += 1
        return
    for i in case:
        if i not in ans:
            ans.append(i)
            back()
            if cnt == num:
                return ans
            ans.pop()
    
try:
    while True:
        testcase, num = input().split(' ')
        num = int(num)
        case = list(testcase)
        cnt = 0
        ans = []
        result = back()
        if math.factorial(len(testcase)) < num:
            print(testcase, num, "=", "No permutation")
        else:
            print(testcase, num, "=", "".join(map(str, result)))
except:
    exit()


