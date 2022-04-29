# time_hour = time // 60
# time_min = time % 60
# hour += time_hour
# minute += time_min
# if min >= 60 -> hour += 1, min = min - 60
# if hour >= 24 -> hour = hour - 24

hour, minute = map(int, input().split())
time = int(input())
time_hour = time // 60
time_min = time % 60

if time >= 0:
  hour += time_hour
  minute += time_min
  if minute >= 60:
    hour += 1
    minute -= 60
  if hour >= 24:
    hour -= 24
  print(hour, minute)
