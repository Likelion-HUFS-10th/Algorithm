import sys

word = sys.stdin.readline()
count = len(word)-1

count = count - word.count('=')
count = count - word.count('-')
count = count - word.count('nj')
count = count - word.count('lj')
count = count - word.count('dz=')
print(count)