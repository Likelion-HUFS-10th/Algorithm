n = int(input()) #몇번째 영화인지
idx = 0
temp = n
new_arr = []
while temp>0:
    if '666' in str(idx):
        temp -=1
        new_arr.append(idx)
    idx+=1

print(new_arr[-1])