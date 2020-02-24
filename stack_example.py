# word = input('Input a word:')
# word_list = list(word)
# print(word_list)
# for i in range(len(word_list)):
#     print(word_list.pop(), end='') #end는 줄바꿈 없이. 전체주석 ctrl + /
#

# Decimal to
Two_list = list()
Deci = 1
cnt = 0
while cnt != 10:
    Deci = int(input("Input a decimal:"))
    cnt += 1
    if (Deci > 1):
        while Deci != 0:
            Deci_re = Deci % 2
            Deci = Deci // 2
            Two_list.append(str(Deci_re))
        for i in range(len(Two_list)):
            print(Two_list.pop(),end='')
        print('\n')
    else : break

# Two = 1
# cnt = 0
# while cnt != 10:
#     Two = int(input("Input a Two:"))
#     Two_list = list(str(Two))
#     cnt += 1
#     deci = 0
#     if (Two != 0):
#         for i in range(len(Two_list)):
#             deci = deci + (Two_list(i))*2**i
#         print(deci)
#     else : break
