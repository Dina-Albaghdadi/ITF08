def triangle_area (base, height):
    return 0.5 * base * height
base = int(input("To calculate the area of the triangle enter the base:"))
height = int(input("And enter the height:"))
area = triangle_area(base,height)
print(area)
def circle_area(r):
    return 3.14 * r * r
r = int(input("To calculate the area of the circle enter the radius:"))
area = circle_area(r)
print(area)
def rectangle_area(length, width):
    return length * width
length = int(input("To calculate the area of the rectangular enter the length:"))
width = int(input("And enter the width:"))
area = rectangle_area(length, width)
print(area)