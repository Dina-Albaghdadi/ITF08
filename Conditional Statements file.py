def circle():
    r = int(input("To calculate the area of the circle enter the radius:"))
    circle_area = r*r * 3.14
    print(circle_area)

    if circle_area >= 10:
        print("big")
    elif circle_area<10 and circle_area>0:
        print("small")
    else:
        print("Invalid inputs")


def triangle():
    base = int(input("To calculate the area of the triangle enter the base:"))
    height = int(input("And enter the height:"))
    triangle_area= 0.5 * base * height
    print(triangle_area)

    if triangle_area >= 10:
        print("big")
    elif triangle_area<10 and triangle_area>0:
        print("small")
    else:
        print("Invalid inputs")


def rectangular():
    length = int(input("To calculate the area of the rectangular enter the length:"))
    width = int(input("And enter the width:"))
    rectangular_area=length*width
    print(rectangular_area)



    if rectangular_area >= 10:
        print("big")
    elif rectangular_area<10 and rectangular_area>0:
        print("small")
    else:
        print("Invalid inputs")


circle()
triangle()
rectangular()
#
# #مثال على طريقة حل المهندس
# def add(n1 , n2):
#     sum = n1+n2
#     print(f"{n1}+{n2}=", sum)
#
#
# while True:
#     selection = int(input("""1. Sum
# 2. Subtract
# 3. Multiply
# 4. Division
# 5. Calculate triangle area
# 6. Calculate circle area
# 7. Calculate rectangle area
# 8. Exit"""))
#     if selection == 1:
#         n1 = int(input("Enter number one"))
#         n2 = int(input("Enter number two"))
#     elif selection == 8:
#         exit()
# add(n1=n1,n2=n2)