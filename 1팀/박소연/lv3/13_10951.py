# 무한루프 -> while문
# 런타임에러 -> try-except 구문
# 1) 에러 발생해도 프로그램이 멈추지 않고 계속 진행하도록 만듦
# 2) try: ~ except: break
# 3) try문 : 에러가 발생할 가능성이 있는 문장 작성
# 4) excpet문 : 에러 발생 시 실행시킬 문장 작성
# 5) 에러가 없을 경우 - try 실행 -> except 지나침 -> 그 다음 코드 진행
# 6) 에러가 있을 경우 - try 실행 -> except 실행
# 7) try - except - else(에러가 발생X 실행) - finally(무조건 실행)

while True:
  try:
    a, b = map(int, input().split())
  except:
    break
  print(a + b)