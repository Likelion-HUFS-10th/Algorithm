# 현재시간 - 45분
# min - 45 < 0 -> min = 60 - (45 - min), hour -= 1
# min - 45 > 0 -> min = min - 45

hour, minute = map(int, input().split())

if minute - 45 < 0:
  minute = 60 - (45 - minute)
  hour -= 1
  if hour < 0:
    hour = 24 + hour
  print(hour, minute)
else:
  minute = minute - 45
  print(hour, minute)
