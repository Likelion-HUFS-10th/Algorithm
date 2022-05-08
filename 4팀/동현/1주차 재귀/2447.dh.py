"""
혼자 하는데 한계가 있어서 참고하며 작성했습니다ㅠㅠㅠ
첫번째 줄은 그대로, 두번째 줄은 빈칸이 발생, 세번째 줄은 그대로
그대로 입력 받는 것과 빈칸은 n에 따라 모양이 달라짐 -> 재귀로 구현

재귀가 필요한 부분을 파악하고 이를 적절히 사용하는게 중요
"""

n = int(input())

def draw_star(num):
    if num == 3: # num이 3일 경우를 기본값으로 지정
        return ['***','* *','***']

    star_arr = draw_star(num // 3) # 재귀 사용으로 이전의 값을 가져옴 -> 구현하고 싶었던 부분 => 재귀로 해결 가능
    stars = []

    for i in star_arr: # 첫번째 줄
        stars.append(i * 3)

    for j in star_arr: # 두번째 줄
        stars.append(j + ' ' * (num//3) + j) # n에 따라 빈칸의 개수가 증가함을 반영

    for k in star_arr: # 세번째 줄
        stars.append(k * 3)

    return stars # n에 따른 결과값

print('\n'.join(draw_star(n))) # 리스트인 stars에 담긴 요소들을 개행을 기준으로 나눠서 print함