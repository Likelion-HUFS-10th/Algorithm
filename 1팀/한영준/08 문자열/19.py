import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
lst.remove("NULL") # 쉬운 편집을 위해 null도 제거
opp = ""

m,n = 2,4 # readline 통해서 받으면 되는데 일단 예제값으로 설정해둠

for i in range (0,m) :
    opp = opp + " " + lst[i]

for i in range (n,m,-1) : # 인덱스 역순으로 붙여줌
    opp = opp + " " + lst[i]

for i in range (n,len(lst)) :
    opp = opp + " " + lst[i]

opp = opp + " NULL" # null을 붙여 원래 형식을 맞춤

opp_list = list(opp.split()) #공백 기준 쪼개서 리스트화
opp_list = "->".join(opp_list)
#뒤집은 리스트의 값들 사이에 ->를 넣으면서 순서대로 출력

print(opp_list)