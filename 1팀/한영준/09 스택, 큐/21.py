lines = input()
lines = sorted(lines)
del_list = []

for chr in range(len(lines)-1):
    if lines[chr] == lines[chr+1]:
        del_list.append(chr)
        
for i in del_list:
    lines[i] = "0"

for k in range(len(del_list)): 
    #remove는 한번만 실행되므로 지워야될 수만큼 반복
    lines.remove("0")

print (lines)