import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
lst.remove("NULL")
opp = ""

for i in range (0,len(lst),2) :
    opp = opp + " " + lst[i]

for i in range (1,len(lst),2) :
    opp = opp + " " + lst[i]

opp = opp + " NULL"

opp_list = list(opp.split())
opp_list = "->".join(opp_list)

print(opp_list)