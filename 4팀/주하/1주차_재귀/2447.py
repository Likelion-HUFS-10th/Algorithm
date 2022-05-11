'''
저도 기억이 안 나서 다른 풀이를 참고해서 작성했습니다..

'''
n = int(input())
cnt = 0

def stars(n):
    star_list = []
    for i in range(len(n)*3):
        if i // len(n) == 1:
            star_list.append(n[i % len(n)]+ " " * len(n) + n[i % len(n)])   # 가운데 공백
        else:
            star_list.append(n[i % len(n)] * 3)
    return star_list

star_str = ["***", "* *", "***"]

while n > 3:
    n //= 3
    cnt += 1

for _ in range(cnt):
    star_str = stars(star_str)

for j in star_str:
    print(j)