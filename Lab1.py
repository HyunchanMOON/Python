Born = int(input("태어난 년도를 입력하세요? "))

Age = 2019 - Born +1

if  26 >= Age and Age >= 20 :
    school = 'University'
elif 20 > Age and Age >= 17 :
    school = 'HighSchool'
elif 17 > Age and Age >= 14 :
    school = 'MiddleSchool'
elif 14 > Age and Age >= 8  :
    school = 'ElementrySchool'
else : school = '학생이 아닙니다.'
print(school)
