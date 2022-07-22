"""
build_frame = [x, y, a, b]
(x, y) -- 기둥 또는 보를 설치, 삭제할 교차점의 좌표
a -- 설치 또는 삭제할 구조물의 종류 // 0은 기둥, 1은 보
b -- 구조물을 설치할 지 삭제할지 // 0은 삭제, 1은 설치

교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽으로 설치 및 삭제

return 형식
--
[x, y, a]
(x, y) -- 기둥, 보의 교차점
a -- 구조물의 종류]
x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬
"""

n = int(input())
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

def possible(answer):
	for x, y, stuff in answer:
		if stuff == 0:
			if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
				continue
		
			return False
		
		elif stuff == 1:
			if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer and [x+1, y, 1] in answer:
				continue
			return False

	return True

	
def solve(n, build_frame):
	answer = []

	for frame in build_frame:
		x, y, a, b = frame

		# 삭제하는 경우
		if b == 0:
			answer.remove([x, y, a])
			if not possible(answer):
				answer.append([x, y, a])
		
		# 설치하는 경우
		else:
			answer.append([x, y, a])
			if not possible(answer):
				answer.remove([x, y, a])

	return sorted(answer)

print(solve(n, build_frame))
