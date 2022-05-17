#0. 내 풀이
def reverseString(s: str):
    s_lst = [i for i in s]
    s_lst_reversed = list(reversed(s_lst))
    reversed_s = "".join(s_lst_reversed)
    return reversed_s

#1. 투 포인터를 이용한 스왑.
'''
투 포인터를 이용한 스왑이란, 쉽게 말해
양쪽 끝에 커서를 두고 좁혀오면서 반대쪽의 것과 값을 같도록 바꿔주는 것을 반복하는 것.
이 반복이 수행되는 조건은 left의 값(left index 값)이 오른쪽의 것보다 작은 조건 하에서만 수행되는 것.
'''
def reverseString(self, s:list) -> None:
    left = 0 # 첫 번째 포인터
    right = len(s) - 1 # 두 번 째 포인터 / 인덱스니까 수를 1 낮춰주기.
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
