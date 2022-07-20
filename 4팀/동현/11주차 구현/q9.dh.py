"""
처음에는 삼중 반복문으로 접근 => 이중반복문으로 해결 가능, 삼중반복시 파악의 어려움
길이의 절반 만큼만 반복 가능
처음부분부터 반복이 가능할때까지 반복 => 불가능해진 부분에서 문장을 바꿔줌
문장(s)를 직접 바꿀 경우 인덱스 문제가 발생 => 새로운 문장을 만들어주는 형태로 진행
반복하는 부분을 조건에 따라 갱신해줘야함
"""
def solution(s):
    x = len(s) // 2
    count_list = []
    for i in range(1, x+1):
        count = 1
        y = ''
        repeat = s[:i] # 이부분이 핵심적인 부분! => 반복이 중단된 경우 새로 반복할 부분을 새롭게 만들어줘야함
        
        
        for j in range(i,len(s),i):
            if repeat == s[j:i+j]:
                count += 1
            else:
                if count == 1:
                    y = y + repeat
                else:
                    y = y + str(count) + repeat
                repeat = s[j:j+i]
                count = 1
                
        if count != 1:
            y = y + str(count) + repeat
        else:
            y = y + repeat
        
        count_list.append(len(y))
        
    return min(count_list)

s = "aabbaccc"
print(solution(s))