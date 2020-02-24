dan = 1
while(dan>0):
    dan = int(input('구구단 몇단을 계산할까요?'))
    if(dan == 0):
        break
    elif(dan>9 or dan<2):
        print('2~9 까지의 수를 입력하세요')
    else :
        for a in range(1,10):
            cal = dan * a
            print(dan, '*', a, '=', cal)
print('구구단을 종료합니다.')



# dan = int(input("구구단 몇단을 계산할까요? "))
#
# while dan <= 0 or dan >9:
#     if
#     dan = int(input("다시 입력해주세요"))
#
# print("구구단", dan, "단을 계산합니다.")
#
# for i in range(1, 10):
#     cal = dan * i
#     print(dan, "x", i, "=", cal)
