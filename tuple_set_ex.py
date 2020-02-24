a = (1,2,3)
pirnt(type(a))
a=(1) # int type
a=(1,) # tuple type


##set 은 중복을 불허하는 자료형

set_1 = set([1,2,3,4,5,1,2,3,4,5])

set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set1 | set2 # 합집합

set1.union(set2) #합집합

set1-set2 #차집합

set1 & set2 #교집합

set1.intersection(set2) #r교집합

set1.difference(set2) #차집합
