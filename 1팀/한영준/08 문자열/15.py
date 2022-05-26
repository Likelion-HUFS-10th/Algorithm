import sys 

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
opp = ""

for i in range (len(lst)) :
    if lst[i] == "NULL":
        opp = opp + " " + lst[i] #NULL은 opp 맨뒤에 붙여줌
    else: 
        opp = lst[i] + " " + opp

opp_list = list(opp.split()) #공백 기준 쪼개서 리스트화
opp_list = "->".join(opp_list) 
#뒤집은 리스트의 값들 사이에 ->를 넣으면서 순서대로 출력

print(opp_list)

