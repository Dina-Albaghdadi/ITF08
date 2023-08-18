my_list=[]
numbers = int(input("Enter the total number of numbers:"))
for i in range(0,numbers):
    n = int(input(f"Enter number{i+1}:"))
    my_list.append(n)
    my_list = my_list.sort
    print("Max number=:", my_list[-1])
    print("Min number=:", my_list[0])

