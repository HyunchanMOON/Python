# Byear = int(input("태어난 연도를 입력하세요:"))
# age = 2020 - Byear + 1
# print(age)
#
# if 20<=age and age<=26:
#     School = '대학생'
# elif 17<=age and age<20:
#     School = '고등학생'
# elif 14<=age and age<17:
#     School = '중학생'
# elif 8<=age and age<14:
#     School ='초등학생'
# else: School ='학생이 아닙니다.'
#
# print(School)


BYear = int(input('태어난 년도를 입력하세요:'))

Age = (2019-BYear) + 1
print(Age)

if 20<=Age<=26: #and 조건으로 나눠주는게 좋다.
    School = '대학생'
elif 17<=Age<20:
    School = '고등학생'
elif 14<=Age<17:
    School = '중학생'
elif 8<=Age<14:
    School = '초등학생'
else : School = '학생이 아닙니다.'
print(School)
