n = int(input())

def f(n):
    if n == 0 or n == 1:                 # 0번째 피보나치 수는 0 / 1번째 피보나치 수는 1
        return n
    
    return f(n-1)+f(n-2)                 # n번째 피보나치 수는 ->  Fn = Fn-1 + Fn-2 

print(f(n))
