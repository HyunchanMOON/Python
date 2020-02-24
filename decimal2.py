decimal = int(input("10진수 입력"))
re = ''

while decimal>0:
    remainder = decimal % 2 #나머지값
    decimal = decimal // 2
    re = str(remainder) + re
print(re)
