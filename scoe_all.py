def calculate(x,y):
    total = x + y   #새로운 값 할당 되어 함수 내 total은 지역변수가 된다.
    print("In Function")
    print("a:", str(a), "b:", str(b), "a+b:", str(a+b), "total:", str(total))
    return total

a = 5 # a와 b는 전역변수
b = 7
total = 0 # 전역변수 total
print("In Program -1")
print("a:", str(a), "b:", str(b), "a+b:", str(a+b))

sum = calculate(a,b)
print("After Calculation")
print("Total:", str(total), \
    "Sum:", str(sum))
