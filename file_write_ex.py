##파일 쓰기 예제

f = open("count_log.txt", 'w', encoding="utf8")
for i in range(1, 11):
    data = "%d 번째 줄입니다.\n" % (i)
    print(data)
    f.write(data)
f.close()

##내용 추가시 w를 쓰면 기존 파일에 덮어쓰는게 된다. a를 써야 추가된다.

f = open("count_log.txt", 'a', encoding="utf8")
for i in range(11, 21):
    data = "%d 번째 줄입니다.\n" % (i)
    print(data)
    f.write(data)
f.close()

os.path.isdir("abc")
