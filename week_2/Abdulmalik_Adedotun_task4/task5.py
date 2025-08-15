students_name = []
students_score = []
student_name = input("Enter the three student name: ")
students_name.append(student_name)
student_score = input("Enter the student score: ")
students_score.append(student_score)
for i in students_name, students_score:
    if len(students_name) == len(students_score):
        students_name[i] = students_score[i]
        print(f"{students_name} - {students_score}")


