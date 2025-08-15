'''# 2. Shopping list manager
shopping = []
shopping_list1 = input("Enter your first shopping item: ")
shopping.append(shopping_list1)
shopping_list2 = input("Enter your second shopping item: ")
shopping.append(shopping_list2)
shopping_list3 = input("Enter your third shopping item: ")
shopping.append(shopping_list3)
'''
shopping = []
for i in range(3):
    shopping_list = input(f"Enter the Item we are shopping {i+1}: ")
    shopping.append(shopping_list)
print([shopping_list for shopping_list in shopping])