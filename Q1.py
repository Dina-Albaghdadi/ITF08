#Q1
n = int(input("Enter 1 0r 2:"))
def numbers():
    if n == 1:
    items = int(input("Enter the total number of items: "))
    my_list =[]
    for i in range(0,items):
        y = int(input(f"Enter item number: {i+1} "))
        my_list.append(y)
        if my_list[0] == my_list[-1]:
            print("plaindrome")
        else:
            print("not plaindrome")
    else:
        x= int(input("Enter the number:"))
        if x%2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
numbers()


