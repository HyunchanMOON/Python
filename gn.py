print("구구단을 계산하는 프로그램입니다.")

x = 1

while(x!=0):
    x = int(input('구구단 몇단을 계산할까요?'))
    if (x == 0):
        print('end')
        break
    elif(x<0 or x>9):
        print('1~9까지의 수를 입력하세요.')
    else:
        for i in range(1,10):
            result = x * i
            print(x, 'x', i, '=', result)


# dan = int(input("구구단 몇단을 계산할까요?"))
# result = 0
#
# print('구구단', dan,'단을 계산합니다.')
#
# for i in range(1,10):
#             result = dan * i
#             print(dan, 'x', i, '=', result)
