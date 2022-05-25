import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
lst = list(line.split("->"))
lst.remove("NULL")
opp = ""

m,n = 2,4

for i in range (0,m) :
    opp = opp + " " + lst[i]

for i in range (n,m,-1) :
    opp = opp + " " + lst[i]

for i in range (n,len(lst)) :
    opp = opp + " " + lst[i]

opp = opp + " NULL"

opp_list = list(opp.split())
opp_list = "->".join(opp_list)

print(opp_list)