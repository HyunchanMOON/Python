## list Comprehension이란
# 기존 List를 사용해서 간단히 다른 List를 만드는 기법
# for 문 없이 새로운 list 생성 가능
# 포괄적 리스트, 지능 리스트, 포함되는 리스트 등으로 표현
# for + append 보다 빠른 속도의 기법



result = []

for i in range(10):
    result.append(i)


##

[i for i in range(10)]



text_1 = "Hello"
text_2 = "World"

[a+b for a in text_1 for b in text_2]


[a+b for a in text_1 for b in text_2 if a==b]

==

for a in text_1:
    for b in text_2:
        print(a+b)


[[a+b for a in text_1] for b in text_2]
# 밖에 있는 for 문이 먼저 돌고 안에 있는 for 문이 나중에 돈다.

#ex
test_1 = "CBA"
test_2 = "FGA"
example = [a+b for a in test_1 for b in test_2]
example.sort()

#ex2
words = "the quick brown fox jumps over the lazy dog".split()
words
[word for word in words]
[len(word) for word in words]
[len(word),word.upper()] for word in words]
[len(word),word.upper(),word.lower()] for word in words]
