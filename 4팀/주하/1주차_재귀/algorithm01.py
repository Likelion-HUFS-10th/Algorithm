n = int(input()) 

def factorial(n):   
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))


'''
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2 * 1

입력 형식 잘 확인하기!

1 ≤ N ≤ 12 라고 생각해서
if n == 1:
    return n 으로 작성했는데 런타임 에러 발생

0 ≤ N ≤ 12
n이 0일 수도 있음 -> 0! = 1,
따라서 if n == 0:
         return 1로 해줘야 함.

        if n <= 1:
         return 1 이것도 가능.
    

'''
