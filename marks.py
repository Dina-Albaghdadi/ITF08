students = int(input("Enter the number of the students:"))
for i in range (students):
    marks_number = int(input("Enter total marks number:"))
    marks = []
    for j in range(marks_number):
        mark = float(input(f"Enter student {i+1} mark {j+1}:"))
        marks.append(mark)
    average = sum(marks)/ len(marks)
    print(f"student{i+1} average =", average)
    print(f"max mark for student {i+1} =", max(marks))
    print(f"min mark for student {i+1} =", min(marks))