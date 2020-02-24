# def f(x):
#     return 2*x + 7
# def g(x):
#     return x**2
# x = 2
# print(f(x) + g(x) + f(g(x)) + g(f(x)))


# def f():
#     s = "I love London!" # 지역 변수와 전역변수에 같은 값을 주려면 변수 앞에 global 입력!
#     print(s)
# s="I love Paris"
# f()
# print(s)


# def f():
#     global s
#     s = "I love London!" # 지역 변수와 전역변수에 같은 값을 주려면 변수 앞에 global 입력!
#     print(s)
#
# s="I love Paris"
# f()
# print(s)


def calculate(x,y):
    total = x+y
    print("In Function")
    print("a:",str(a),"b:",str(b),"a+b:",str(a+b),"total:",str(total))
    return total

a = 5
b = 7
total=0
print("In Program -1")
print("a:",str(a),"b:",str(b),"a+b:",str(a+b))
sum = calculate(a,b)
print("After Calculation")
print("Total:",str(total),"Sum:",str(sum))
