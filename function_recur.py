def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factoral")
n = int(input("n! 연산을 시작합니다. n값을 입력하세요:"))
result = factorial(n)

print(result)
