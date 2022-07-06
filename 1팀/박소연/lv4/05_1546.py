# 성적 수정하기
# 원래 성적 / 성적 중 최대값 * 100 -> 새로운 평균 계산

num = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = []

for elem in score:
  new_score.append(elem / max_score * 100)
print(sum(new_score) / num)