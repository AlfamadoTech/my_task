o_level_subject = input("Enter five O'Level subject relevent to course applied including english and math (seperate it using comma): ").title().split(",")
o_level_grade = input("Enter grade with a minimum grade of C6 with result obtained at one sitting: ").upper().split(",")
o_level_result = dict(zip(o_level_subject, o_level_grade))
print(o_level_result.values())
if o_level_result.values() == "A" or o_level_result.values() == "B"or o_level_result.values() == "C":
    print("Eligible")
else:
    print("Not Eligible")

# print(f"{o_level_resul}\nWaec Result: {o_level_result}")