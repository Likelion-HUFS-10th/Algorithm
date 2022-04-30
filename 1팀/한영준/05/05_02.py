num_list = list(range(1,10001))
a=1
num = 0

def self_number() -> int:
    num_list = list(range(1, 10001))
    a = 1
    num = 0

    #global num_list
    #global a
    #global num

    while a<= 10000 :
    # 2자리 수 a
        if (1<= a // 10 < 10  ):
            num = a + a//10 + a%10
        # 3자리 수 a
        elif (10<= a//10 < 100) :
            num = a + a//100 + (a//10)%10 + a%10
        #4자리 수 a
        elif (100<= a//10 < 1000) :
            num = a + a//1000 + (a//100)%10 + (a//10)%10 + a%10
        elif (a == 10000) :
            num = 10001

        num_list.remove(num)

        a = a+1

    for i in range(len(num_list)-1):
        print (num_list[i])

self_number()



