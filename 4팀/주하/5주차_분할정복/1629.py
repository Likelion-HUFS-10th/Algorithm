'''
시간 초과 - >  재귀 사용

'''
import sys
input = sys.stdin.readline

def divide_multiple(b):
    if b == 1:
        return  a % c        # a랑 c는 참조

    else:
        result = divide_multiple(b//2)
        if b % 2 == 0:
            return result * result % c

        else:
            return result * result * a % c

a,b,c  = map(int,input().split())

print(divide_multiple(b))



#-----------------시간 초과 ------------------#
# import sys
# input = sys.stdin.readline

# def divide_multiple(a,b):
#     if b == 1:
#         return  a%c

#     else:
#         if b % 2 == 0:
#             b = b // 2
#             result = (a**b) * (a**b)
#             return result % c

#         else:
#             b % 2 == 1
#             b = b // 2
#             result = (a**b) * (a**b) * a
#             return result % c

# a,b,c  = map(int,input().split())

# print(divide_multiple(a,b))
