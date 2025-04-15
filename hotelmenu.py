menu ={"Pizza":40,
    "Pasta":50,
    "Fries":20,
    "Kabab":60,
}
print("Welcome to our Restraunt.\n")
for item,price in menu.items():
    print(f"{item}: {price} RS")
    
order_total =0;


while True:
    item=str(input("Select your Items:"))
    if item in menu:
        order_total += menu[item]
        print(f"Your item is selected")
        
    else:
        print("Selected item is not in our menu...")
        
    another_order=input("You want to add another item? (Yes/No)")
    if another_order.lower() != 'yes':
        break
    
print(f"You have to pay a total amount of: {order_total} RS")