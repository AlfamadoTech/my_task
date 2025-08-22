# Unilag Admission Criteria based on Government directive using control flow
candidate_name = input("Enter your name: ").title()
candidate_age = int(input("Enter your age: "))
uni_choice = input("Did you choode UNILAG as your first choice (Yes/No): ").lower()
result_sitting = input("Did you obtain your o_level result at first sitting (Yes/No): ").lower()
utme_score = int(input("Enter your utme score: "))
o_level_subject = input("Enter five O'Level subject relevent to course applied including english and math (seperate it using comma): ").title().split(",")
o_level_grade = input("Enter grade with a minimum grade of C6 with result obtained at one sitting: ").upper().split(",")
o_level_result = dict(zip(o_level_subject, o_level_grade))
print(f"Name: {candidate_name}\nAge: {candidate_age}\nFirst_Choice: {uni_choice}\nUtme SCore: {utme_score}\nOne Sitting: {result_sitting}\nWaec Result: {o_level_result}")
for subject, grade in o_level_result.items():
    if grade == "A":
        print("Allowed")
    elif grade == "B":
        print("Allowed")
    elif grade == "C":
        print("Allowed")
    elif grade == "D":
        print("Not allowed")
    elif grade == "E":
        print("Not allowed")
    elif grade == "F":
        print("Not allowed")
    else:
        print("wrong grade, not eligible")
    if candidate_age >= 16 and uni_choice == "yes" and result_sitting == "yes" and utme_score >= 200 and grade == "A" or "B" or "C":
        print("Eligible for Postutme")
        post_utme_score = int(input("post utme score out of 100: "))
        department = ["College of Basic Medical Science", "College of Engineering", "College of Art and Social Science", "College of Education"]
        if post_utme_score >= 70 and utme_score >= 270:
            print(f"You have been offered admission in {department[0]}")
            course_chosen = input("Course you chose to study: ").upper()
            if post_utme_score >= 90 and utme_score >= 300 and course_chosen == "MEDICINE AND SURGERY":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            elif post_utme_score >= 80 and utme_score >= 280 and course_chosen == "NURSING" or "PHARMACY" or "MLS" or "MEDICAL LAB SCIENTIST":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            elif post_utme_score >= 75 and utme_score >= 275 and course_chosen == "PHYSIOTHERAPY" or "RADIOLOGY" or "NUTRITION AND DIETETICS":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            else:
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
        elif post_utme_score >= 60 and utme_score >= 250:
            print(f"You have been offered admission in {department[1]}")
            course_chosen = input("Course you chose to study: ").upper()
            if post_utme_score >= 70 and utme_score >= 260 and course_chosen == "MECHANICAL ENGINEERING" or "CHEMICAL ENGINEERING" or "CIVIL ENGINEERING" or "COMPUTER ENGINEERING" or "ELECTRICAL AND ELECTRONIC ENGINEERING" or "MECHATRONICS ENGINEERING":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            elif post_utme_score >= 65 and utme_score >= 255 and course_chosen == "COMPUTER SCIENCE" or "ARCHITECTURAL ENGINEERING":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            else:
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
        elif post_utme_score >= 50 and utme_score >= 240:
            print(f"You have been offered admission in {department[2]}")
            course_chosen = input("Course you chose to study: ")
            if post_utme_score >= 50 and utme_score >= 240 and course_chosen == "LAW":
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
            else:
                print(f"Congratulation! you have been offered admission to study {course_chosen}")
        elif post_utme_score >= 40 and utme_score >= 200:
            print(f"You have been offered admission in {department[3]}")
            course_chosen = input("Course you chose to study: ")
            print(f"Congratulation! you have been offered admission to study {course_chosen} Education")
        else:
            print("Sorry postutme score too low for admission")
    else:
        print("Not eligible for postutme")