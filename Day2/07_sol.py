inventory = {
    "laptop": {"price": 50000, "quantity": 5},
    "mouse": {"price": 500, "quantity": 20},
    "keyboard": {"price": 1500, "quantity": 10}
}

def show_product():
    for product in inventory:
        print(f"{product.upper()} : price : {inventory[product]['price']}, quantity : {inventory[product]['quantity']}")


def add_product():
    name = input("Enter name of product :")
    price = int(input("Enter price of product :"))
    quantity = int(input("Enter quantity of product :"))
    
    name = name.lower()
    
    if inventory.get(name):
        print("Product is already in the inventory")
        return;
    
    inventory[name] = { "price": price, "quantity": quantity }
    
    
def update_quantity():
    name = input("Enter name of product :")
    
    name = name.lower()
    if inventory.get(name) == None:
        print("Product is not in the inventory")
        return;
    
    quantity = int(input("Enter quantity of product :"))
    inventory[name]['quantity'] = quantity
    
def search_product():
    name = input("Enter name of product :")
    
    name = name.lower()
    print(name)
    if inventory.get(name):
        print(f"{name} : price : {inventory[name]['price']}, quantity : {inventory[name]['quantity']}")
        return;
    
    print("Product not found")
    
def calculate_inventory():
    for item in inventory:
        print(f"{item} : {inventory[item]['price']}x{inventory[item]['quantity']}")
    

            
while True:
        print(f"""1. Show Products
        2. Add Product
        3. Update Quantity
        4. Search Product
        5. Calculate Inventory Value
        6. Exit""")
        
        n = int(input("Enter a value : "))
        
        match n:
            case 1: show_product()
            case 2: add_product()
            case 3: update_quantity()
            case 4: search_product()
            case 5: calculate_inventory()
            case _: break;
            
