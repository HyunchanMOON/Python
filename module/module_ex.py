import fah_converter as fc #모듈을 줄여서 말하는것 as)
result = fc.convert_c_to_f(40)
print(result)

#====
#from fah_converter import convert_c_to_f
#result = convert_c_to_f(40)
#print(result)

##import fah_converter import* #모듈에서 모든함수 호출하기


# 각 module 예시

import random
random.random() * 1000 //10


import time
time.localtime() #현재시간 쪼개서 보기

import datetime
datetime.datetime.strptime("20/02/2020","%d/%m/%Y").strftime("%Y-%m-%d")

import urllib.request
response = urllib.request.urlopen("http://www.google.com")
response.read()

#빌트인 모듈 구글에 검색 or docs.python.org 에서 공식문서 읽기
