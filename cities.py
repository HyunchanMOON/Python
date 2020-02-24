cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6], "AND", cities[-8:]) # cities 번수의 0부터 5까지 , -9부터 끝까지
print(cities[:]) # cities 변수의 처음부터 끝까지
print(cities[-50:50]) # 범위를 넘어갈 경우 자동으로 최대 범위를 지정
print(cities[::2], "AND", cities[::-1]) # 2칸 단위로, 역으로 슬라이싱
