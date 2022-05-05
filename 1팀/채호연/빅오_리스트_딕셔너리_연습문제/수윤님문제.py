'''
1. 다음 선지 중 틀린 것을 모두 골라 올바르게 고치시오.

ㄱ. 불변 객체(Immutable object)는 bool, int, str, tuple 총 4개이다.
ㄷ. Numpy는 C로 만들어진 모듈이다.
ㄴ. 파이썬은 원시 타입 형태 자료형을 아예 지원도 하지 않는다.
ㅁ. O(n). 계수를 제하고 최고차항만 표기하기 때문이다.
'''

#2번
drink_count = int(input("아샷추를 일주일 중 몇 번 드시겠습니까? "))
if drink_count <0 or drink_count > 8:
    print("그렇게는 못 먹어요.")
else:
   shot_per_day = list(map(int, input("먹을 아샷추의 개수를 입력하세요").split()))
   print(sum(shot_per_day))
   
   if sum(shot_per_day) > 10:
       print("우욱,,,")
   else:
       print("내일 또 먹어야지.")
       shot_per_day.append("배부르다")
       print(shot_per_day)