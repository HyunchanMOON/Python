import numpy as np

A = np.array([[4, -5],[-2,3]])
b = np.array([[-13],[9]])

x = np.linalg.inv(A).dot(b)   # linalg :선형 대수식을 사용하겠다. linalg.dot -> 선형대수중 내적연산을 사용하겠다.
print(A,b)

print(x)
