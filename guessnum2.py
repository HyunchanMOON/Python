import random
R = random.randint(1,100)
cnt = 1
i = int(input('맞춰보세요?'))
while i != R :
    if i>R :
        print('down')
    elif i<R :
        print('up')
    i = int(input('다시\n'))
    cnt = cnt + 1
    if cnt == 5:
        break
else : print('fin')




# import random
# i = random.randint(1,100)
# print("5회 안에 숫자를 맞춰보세요?")
# cnt = 1
# n = int(input())
# while n != i:
#     if(n>i):
#         print("Down")
#     elif(n<i):
#         print("Up")
#     n = int(input())
#     cnt = cnt + 1
#     if(cnt == 5):
#         print("초과")
#         break
# else: print("fin")
