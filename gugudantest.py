n = int(input('구구단 몇단?'))

while n != 0:
    if ( n > 9) :
        print('잘못 입력 하셨습니다.')
        n = int(input('다시'))
    else :
        for i in range(1,10):
            print(n, "X" , i, "=", n*i)
        n = int(input('next input'))
print("구구단 게임을 종료합니다.")

# print("몇단?")
# x = 1
# while (x != 0):
#     x = int(input())
#     if x == 0: break
#     if not(1 <= x <=9):
#         print("잘못입력하였습니다.")
#         continue
#     else:
#         print("구구단"+str(x) + "단을 계산합니다.")
#         for i in range(1,10):
#             print(str(x) + "X" + str(i) + "=" + str(x*i))
#         print("구구단 몇 단을 계산할까요?(1~9)?")
# print("종료")
