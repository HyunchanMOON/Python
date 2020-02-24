# def calculate_rectangle_area(x,y):
#     return x*y
#
#
# r_x = 10
# r_y = 20
#
# area = calculate_rectangle_area(r_x, r_y)
#
# print('사각형의 넓이는', area)


# def calculate_rectangle_area(x,y):
#   return x*y
#
# rectangle_x = 10
# rectangle_y = 20
# print("사각형 x의 길이: ", rectangle_x)
# print("사각형 y의 길이: ", rectangle_y)
#
#
# print("사각형의 넓이: ", calculate_rectangle_area(rectangle_x, rectangle_y))

# f(x) = 2x+7, g(x) = x^2, x= 2 일때 f(x) +g(x)+f(g(x)) + g(f(x)) 값은?
# f(2) = 11, g(2) = 4, f(g(x)) = 15,
# g(f(x))=121

def f(x):
    return 2*x +7
def g(x):
    return x**2
    
print('2x+7+x^2+2x^2+7+(2x+7)^2, x=2 일때 결과는?')

x = int(input('x값을 입력하세요:'))
fun = f(x) + g(x)+f(g(x))+g(f(x))
print('결과는',fun,'입니다.')
