f = open("yesterday.txt", 'r') #파일 읽기,
yesterday_lyric = ""
while 1:
    line = f.readline() # 한줄씩 읽어오는 코드
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"  #strip 문자열 양끝의 공백과 \n 지워주는 함수

f.close()
#print(yesterday_lyric)
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY") #upper 모두 대문자로 바꿔라.
print ("Number of a Word 'Yesterday'", n_of_yesterday)
