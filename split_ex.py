split 함수 : string type의 값을 나눠서 List 형태로 변환하는 함수

items = 'zero one two three'.split()
print (items)

example = 'python,jquery,javascript'
print(example.split("y")) # 괄호안에 값은 기준값

example = 'hunet.co.kr'
subdomain, domain, tld = example.split('.')
print(subdomain, domain, tld)
