#Q1
def numbers():
    n = int(input("Enter the number:"))
    if n == 1:
        my_list=[]
        if my_list[0] == my_list[-1]:
            print("plaindrome")
        else:
            print("not plaindrome")
    else:
        if n%2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
numbers()


