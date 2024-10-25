# Menu of the Bajwa resturant
menu = {
    "pizza":1000,
    "burger":350,
    "pasta":400,
    "salad":200,
    "coffee":250, 
}
#Greetings
print("Welcome to Bajwa resturant")
print("pizza: Rs1000\n burger:Rs350\n pasta:Rs400\n salad:Rs200\n coffee:Rs250")
order_total = 0
item_1 = input("Enter the item name: ")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else: 
    print(f"Ordered item{item_1} is not available yet ")

another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2=input("Enter the second item = ")
    if item_2 in menu:
      order_total+=menu[item_2]
      print(f"Ordered item {item_2} has been added to order")
    else: 
        print(f"Ordered item{item_2} is not available")
print(f"The total amount of items is {order_total}")


