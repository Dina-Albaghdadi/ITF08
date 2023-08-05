def circle():
    r = int(input("Enter the raduis:"))
    area = r * r * 3.14
    circle_area=area
    perimeter =2*3.14*r
    print(circle_area)
    print(perimeter)
circle()

def Triangle():
        base = int(input("Enter the base:"))
        height = int(input("Enter the height:"))
        side = int(input("Enter the side of the triangle:"))
        area = 0.5 * base * height
        Triangle_area=area
        perimeter = side * 3  # محيط مثلث متساوي الأضلاع
        print(Triangle_area)
        print(perimeter)

Triangle()
def rectangular():
    length = int(input("Enter the length:"))
    width = int(input("Enter the width:"))
    area=length*width
    rectangular_area=area

    print(rectangular_area)
rectangular()


    if area >= 10:
        print("big")
    elif area >0 and area <10 :
        print("small")
    else:
         print("invalid input")

circle()