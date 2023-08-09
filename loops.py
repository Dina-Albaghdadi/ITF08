def sum_function():
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    sum = n1 + n2
    print(sum)

def sub_function():
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    sub = n1 - n2
    print(sub)

def multiply_function():
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    mul = n1 * n2
    print(mul)

def division_function():
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    div = n1 / n2
    print(div)

def triangle_area():
    base = int(input("To calculate the area of the triangle enter the base:"))
    height = int(input("And enter the height:"))
    area = 0.5 * base * height
    print(area)

def circle_area():
    r = int(input("To calculate the area of the circle enter the radius:"))
    area = 3.14 * r ** 2
    print(area)

def rectangular():
    length = int(input("To calculate the area of the rectangular enter the length:"))
    width = int(input("And enter the width:"))
    rectangular_area = length * width
    print(rectangular_area)

while True:
    selection = int(input("1.Sum\n2.Sub\n3.Multiply\n4.Division\n5.Calculate triangle area\n6.Calculate circle area\n7.Calculate rectangle area\n8.Exit"))
    while True:
        if selection<=8 and selection>=1:
            break
        else:
            selection = int(input("INVALID INPUT, please enter a valid selection")) #عشان يقدر يدخل رقم تاني بس تطلعله هاي الجملة
    if selection == 1:
        sum_function()

    elif selection == 2:
        sub_function()

    elif selection == 3:
        multiply_function()

    elif selection == 4:
        division_function()

    elif selection == 5:
        triangle_area()

    elif selection == 6:
        circle_area()

    elif selection == 7:
        rectangular()

    elif selection == 8:
        print("Bye")
        exit()