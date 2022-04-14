n = int(input())

"""

n이 9라면 어떻게 될지 우선 써보기
-> 처음에는 for 문을 각 인덱스별로 생각함 + 0,1,2 와 같이 하드코딩으로 함
-> 정말 9라면 어떻게 될지! 만 생각함 (하드코딩을 하더라도 하고 나서 패턴을 보려고 노력하자..!)
-> 시간이 더 넉넉했다면 풀 수 있었을 것 같기도 함

"""

#만약 n이 9

def star(n):
    if n==3: #종료조건은 맞음. 
        star_str_ex = ["***","* *","***"] #기본 문자열
        return star_str_ex
    else:
        star_str_ex = star(n//3) #반환된 이전 패턴
        star_str = []
        for i in range(n//3):
            star_str.append(star_str_ex[i]*3)
        for i in range(n//3):
            if i%3==0:
                star_str.append(star_str_ex[i]+" "*(n//3)+star_str_ex[i])
            elif i%3==1:
                star_str.append(star_str_ex[i]+" "*(n//3)+star_str_ex[i])
            else:
                star_str.append(star_str_ex[i]+" "*(n//3)+star_str_ex[i])
        for i in range(n//3):
            star_str.append(star_str_ex[i]*3)
        

        return star_str #다음 패턴에게 넘겨주기 위해서! or 출력하기 위해서 

return_str = star(n)
# print(return_str)
for re in return_str:
    print(re)


