# Store Inventory
store = {"Book": 10, "Pen": 20, "Bag": 5}
print(f"Before Purchase: {store}")
item_to_buy = input("What do you want to buy: ")
item_quantity = int(input("How many do you want: "))
x = store["Book"]
y = store["Pen"]
z = store["Bag"]
x -= item_quantity
y -= item_quantity
z -= item_quantity
print(f"After Purchase: Book : {x}, Pen : {y}, Bag : {z}")