# students = int(input("Enter the number of the students:"))
# for i in range (students):
#     marks_number = int(input("Enter total marks number:"))
#     marks = [];
#     for j in range(marks_number):
#         mark = float(input(f"Enter student {i+1} mark {j+1}:"))
#         marks.append(mark)
#     average = sum(marks)/ len(marks)
#     print(f"student{i+1} average =", average)
#     print(f"max mark for student {i+1} =", max(marks))
#     print(f"min mark for student {i+1} =", min(marks));
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