print("구구단 몇단을 계산 할까요?")
n = int(input())


while n <=0 or n >9 :
    n = int(input("다시 입력해주세요"))

for i in range(1,10):
    print(n, "X" , i, "=", n*i)
