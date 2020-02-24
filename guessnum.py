import random
i = random.randint(1,100)
print('10회 안에 맞추셔야합니다.')
c = int(input('숫자를 맞춰보세요'))

cnt = 0
while(i != c):
    if(i > c):
        print('UP')
    elif(i < c):
        print('DOWN')
    else:
        print("end")
    c = int(input('숫자를 맞춰보세요'))
    cnt +=1
    if(cnt>=10):
        break

if(i==c and cnt<10):
    print('정답입니다!', c,'입니다.')
else:
    print('횟수초과입니다.')
