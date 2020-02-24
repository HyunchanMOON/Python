## ditionary 예

student_info = {20140012:'Sungchul',
20140059:'Jiyong', 20140058:'JaeHong'}


country_code = {}   #dictionary 생성
country_code = {82:'Korea', 1:'USA'}
print(country_code)
country_code.keys()
country_code.items()
country_code.values()
country_code[83] = 'Japan'


for k, v in country_code.items(): # k 는 key값에 들어가고, v는 values 값에 들어간다!
    print(k,v)
