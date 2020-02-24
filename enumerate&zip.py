###enumerate, dict type과 같이 자주 사용한다.

test = 'abcde'
list(enumerate(test))  #enumerate: index numbering 해주는 것!

#ex
test = "Hello World Python"
onehot = test.split()
for i,v in enumerate(onehot):
    print(i,v)


###zip, 두개의 list에서 같은 위치에 있는 값을 뽕아주는것

a = [1,2,3]
b = [10,20,30]
for c in zip(a,b):
    print(c)


a = 'abc'
b = 'cde'


#Listcomprehension + zip 사용예
[sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]


alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for c in enumerate(zip(alist,blist)):
    print(c)
