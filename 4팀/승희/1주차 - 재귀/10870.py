n = int(input())

"""
피보나치
fn = fn-1+fn-2

"""

def cal(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return cal(num-1)+cal(num-2)

print(cal(n))