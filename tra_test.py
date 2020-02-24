def addition(x,y):
    return x + y

def multiplication(x,y):
    return x * y

def divided_by_2(x):
    return x / 2
#python shell 에서 debugging

def main():
    base_line = float(input("밑변의 길이는?"))
    upper_edg = float(input("윗변의 길이는?"))
    height = float(input("높이는?"))
    Area = divided_by_2(addition(base_line,upper_edg)*height)
    print("넓이는:", Area)


if __name__ == '__main__':
    main()
