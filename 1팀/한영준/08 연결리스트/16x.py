import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n")
line = line.strip("\n")
lst = list(line.split("->"))
opp = ""

for i in range (len(lst)) :
    opp = lst[i] + " " + opp

opp_list = list(opp.split())
opp_list = "->".join(opp_list)

print(opp_list)


# line = sys.stdin.readline()
# lst = []
# for num in line :
#     if num.isdigit():
#         lst.append(num)

