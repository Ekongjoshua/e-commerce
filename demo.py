import json
import pprint

SIZE_OF_PRODUCTS = 5
LAST_INDEX = 0
CART = []

db_file = open("/home/goggle20/Desktop/project_place2/json_demo/demo.json")
product_db = json.load(db_file)
db_file.close()

LENGTH = len(product_db)

def view_products(products):
    global LAST_INDEX
    if LAST_INDEX>=LENGTH:
        LAST_INDEX = 0


    next_index = LAST_INDEX + SIZE_OF_PRODUCTS
    x = product_db[LAST_INDEX: next_index]
    return x

        
def add_to_cart(product):
    CART.append(product)
    print("product added to cart")
    
while True:
    print('1)view products\n 2)view cart\n 3)quit')
    choice = input("type here> ")
    if choice == "1":
        for prod in view_products(product_db):
            detail = f"""
            ID: {prod["id"]}
            PRODUCT NAME: {prod["title"]}
            PRICE: {prod["price"]}
            """
            print(detail)
        
            

            print("enter any key to next")
            print("enter product id to add to cart and 'q' to quit dispay")
            choice = input("type here> ")
            if choice == "q":
                break
            elif choice.isdigit():
                product_index = int(choice)-1
                add_to_cart(product_db[product_index])
        
    elif choice == "2":
        if CART:
            for prod in CART:
                detail = f"""
                ID: {prod["id"]}
                PRODUCT NAME: {prod["title"]}
                PRICE: {prod["price"]}
                """
                
                print(detail)
            
        else:
            print("cart is empty ")

        print("enter 'Y' to check out or 'q' to go back to menu")
        choose1 = input("type> ")
        if choose1.upper() == "Y":
                total = 0
                for prod in CART:
                    detail =f"""
                    {prod["price"]}
                    {prod["title"]}
                    {prod["id"]}
                    """
                    total+=prod["price"]
                print("total cart item(s): ", total)
                print()
        
                
        
                print("enter 'Y' procceed to payment or 'q' to cancel payment")
                print()
                cmd = input("type> ")
                if cmd.upper()== "Y":
                    cvv= input("enter your cvv  number: ")
                    address = input("enter your home address: ")
                    bank = input("enter the 10 digit of your atm card; ")
                    print(total, "paid succcessful")
                    print()
                elif cmd.lower() == "q":
                    break
        elif choose1.lower()== "q":
            view_products(detail)
            print()       
    elif choice == "3":
            break
    

    
            
        


