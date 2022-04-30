import sys

word = sys.stdin.readline()
sec = 0
for i in range(len(word)):
    if word[i] == "A" or word[i] == "B" or word[i] == "C":
        sec = sec+3
    elif word[i] == "D" or word[i] == "E" or word[i] == "F":
        sec = sec+4
    elif word[i] == "G" or word[i] == "H" or word[i] == "I":
        sec = sec+5
    elif word[i] == "J" or word[i] == "K" or word[i] == "L":
        sec = sec+6
    elif word[i] == "M" or word[i] == "N" or word[i] == "O":
        sec = sec+7
    elif word[i] == "P" or word[i] == "Q" or word[i] == "R" or word[i] == "S":
        sec = sec+8
    elif word[i] == "T" or word[i] == "U" or word[i] == "V":
        sec = sec+9
    elif word[i] == "W" or word[i] == "X" or word[i] == "Y" or word[i] == "Z":
        sec = sec+10

print (sec)