def solution(numbers):
	temp = []
	answer = ''

	for i in numbers:
		length = len(str(i))
		item = (str(i) * 4)[:4]
		temp.append((item, length))
  
	temp.sort(reverse=True)

	for item, length in temp:
		answer += item[:length]
	
  # "0000"과 같은 경우 0으로 처리하기 위해 정수형으로 변환한 뒤 다시 문자열로 변환
	return str(int(answer))
