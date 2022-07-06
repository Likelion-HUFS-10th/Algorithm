import sys #input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.strip("\n") #readline 으로 받았으니 줄바꿈 제거
lst = list(line.split("->")) #->를 기준으로 쪼개서 리스트로 만들어줌
pellin = "" #뒤집은 리스트를 담아둘 문자열

for i in range (len(lst)) :
    pellin = lst[i] + " " + pellin #끊어서 다시 리스트 형태로 바꾸기 용이하도록 공백 삽입

pellin = list(pellin.split()) #공백 기준으로 쪼개서 리스트화

if lst == pellin:
    print("True")
else :
    print("False")