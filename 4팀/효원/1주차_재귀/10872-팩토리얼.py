num = int(input())

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a-1)

print(factorial(num))


# 이전에 풀었을 땐 result 변수를 만들어 최종값을 관리했지만
# 이번에는 변수 없이 간결한 코드로 구현
