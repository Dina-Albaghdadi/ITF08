def circle():
        r = int(input("To calculate the area of the circle enter the raduis:"))
        circle_area = r * r * 3.14
        print(circle_area)

        if circle_area >= 10:
            print("big")
        elif circle_area<10 and circle_area>0:
            print("small")
        else:
            print("Invalid inputs")


def Triangle():
        base = int(input("To calculate the area of the triangle enter the base:"))
        height = int(input("And enter the height:"))
        Triangle_area= 0.5 * base * height
        print(Triangle_area)

        if Triangle_area >= 10:
            print("big")
        elif Triangle_area<10 and Triangle_area>0:
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
Triangle()
rectangular()
