my_marks = []
number_of_marks = int(input("Enter the total number of marks:"))
for i in range(0,number_of_marks):
    mark = float(input(f"Enter mark {i+1}:"))
    my_marks.append(mark)

average = sum(my_marks) / len(my_marks)
average = round(average,1)
print("The average is:", average)
print('Max mark is:', max(my_marks))
print('Min mark is:', min(my_marks))

