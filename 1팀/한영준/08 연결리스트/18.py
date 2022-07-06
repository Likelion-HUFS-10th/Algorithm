import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
lst.remove("NULL") #쉬운 편집을 위해 null도 제거
opp = ""

for i in range (0,len(lst),2) :
    opp = opp + " " + lst[i] # 홀수 인덱스에 해당하는 값들 우선 모음

for i in range (1,len(lst),2) :
    opp = opp + " " + lst[i] # 위와 같은 방법으로 짝수 인덱스도 모음

opp = opp + " NULL" # null을 붙여 원래 형식을 맞춤

opp_list = list(opp.split()) #공백 기준 쪼개서 리스트화
opp_list = "->".join(opp_list) 
#뒤집은 리스트의 값들 사이에 ->를 넣으면서 순서대로 출력

print(opp_list)