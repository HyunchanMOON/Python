test_que = [1,2,3,4,5]
test_que.append(6)
print(test_que)
for i in range(len(test_que)):
    print(test_que.pop(0), end='')
