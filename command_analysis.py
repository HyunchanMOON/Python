import csv

def getKey(item):   #정렬을 위한 함수
    return item[1]  #신경쓸 필요없음.

command_data = []    # 파일 읽어오기
with open("command_data.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)
command_counter = {}    #dict 생성, 아이디를 key값, 입력
for data in command_data:   #list data를 dict로 변경
    if data[1] in command_counter.keys():   #아이디가 이미 Key값으로 변경되었을 때
        command_counter[data[1]] += 1       #기존 출현한 아이디
    else:
        command_counter[data[1]] = 1        #처음 나온 아이디

diclist = []                    #dict를 List로 변경
for key, value in command_counter.items():
        temp = [key, value]
        diclist.append(temp)
sorted_dict = sorted(diclist, key=getKey, reverse=True)
print(sorted_dict[0:100])
