# Bad Code

# a = 5
#
# if(a>3):
#     print("Hello World")
#     print("Hello Hunet")
# if(a>4):
#     print("Hello World")
#     print("Hello Hunet")
# if(a>5):
#     print("Hello World")
#     print("Hello Hunet")
#

#Good Code

# def print_hello():
#     print("Hello World")
#     print("Hello Hunet")
#
# a = 5
#
# if(a>3):
#     print_hello()
#
# if(a>4):
#     print_hello()
#
# if(a>5):
#     print_hello()

# import math
# a = 1; b = -2; c=1
#
# print((-b + math.sqrt(b**2-(4*a*c)))/(2*a))
# print((-b - math.sqrt(b**2-(4*a*c)))/(2*a))
#

#====================================================================================

import math
def get_result_quadratic_equation(a,b,c):
    values = []
    values.append((-b + math.sqrt(b**2-(4*a*c)))/(2*a))
    values.append((-b - math.sqrt(b**2-(4*a*c)))/(2*a))
    return values

print(get_result_quadratic_equation(1,-8,15))
