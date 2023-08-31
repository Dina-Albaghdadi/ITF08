count = int(input("Enter number of students:"))
# my_list = []
for i in range(0,count):
    marks = int(input(f"Enter number of marks for student {i+1}:"))
    my_list = []
    for j in range(0,marks):
        mark = float(input(f"Enter student {i + 1} mark {j + 1}:"))
        my_list.append(mark)
        avg = sum(my_list) / len(my_list)
        avg = round(avg, 2)
        # print(round(avg, 2))
    print(f"avg for student number {i+1}",avg)
    print(f"max marks for student number {i + 1}", max(my_list))
    print(f"min marks for student number {i + 1}", min(my_list))
    #هذا البرنامج بطبع جملة برينت عادية طب بدي يطبع المعلومات كلها ك dict شو اعمل؟ بعمل dict اسمها std