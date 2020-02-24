# f = open("i_have_a_dream.txt","r")
# contents = f.read()
# print(contents)
# f.close()

#######################################################################################

# with open("i_have_a_dream.txt","r") as f:
#     file_contents = f.read()
#     print(file_contents)

# my_file:
#   contents = my_file.read()
#   print(type(contents),contents)

# with open("i_have_a_dream.txt","r") as f:
#     file_contents = f.read().split("\n")         #file_contents = f.readlines()
#     print(type(file_contents))
#     print(file_contents[:3])



# with open("i_have_a_dream.txt", "r") as my_file:
#     contents


#while 구문 활용

with open("i_have_a_dream.txt","r") as my_file:
    i=0
    while 1:
        line=my_file.readline()   #readline: 한줄씩 읽는, replace:\n는 ""로 바꿔라
        if not line:
            break
        line = line.replace("\n","")
        if line.strip()=="":            #아무것도 없으면 다시 처음으로 가라, 빈칸을 없애주는 코드
            continue
          #line이 없으면 break 해라
        print(str(i)+"==="+line)
        i=i+1


with open("i_have_a_dream.txt", 'r') as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")
    #빈칸을 기준으로 단어를 분리 리스트
    print(word_list)
    line_list = contents.split("\n")
    #한줄 씩 분리하여 리스트


print("Total Number of Characters :", len(contents))
print("Total Number of Words :", len(word_list))
print("Total Number of Lines :", len(line_list))
