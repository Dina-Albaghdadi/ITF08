counter = 0
while True:
    students = []
    number_of_students = int(input("Enter the number of the students:"))
    for i in range(0,number_of_students):
        mark = float(input(f"Enter the number of the marks for student {i+1}:"))
        students.append(mark)
    my_marks = []
    number_of_marks = int(input("Enter the total number of the marks for student:"))
    for i in range(0,number_of_marks):
        mark = float(input(f"Enter mark {i+1}:"))
        my_marks.append(mark)
    average = sum(my_marks) / len(my_marks)
    average = round(average,1)
    print("The average is:", average)
    print('Max mark is:', max(my_marks))
    print('Min mark is:', min(my_marks))
counter +=1
