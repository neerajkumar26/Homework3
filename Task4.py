# Name: - Neeraj Kumar
# ID: - 2047559

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def setName(self, nme):
        self.item_name = nme

    def setPrice(self, val):
        self.item_price = val

    def setQty(self, qty):
        self.item_quantity = qty

    def setDesc(self, des):
        self.item_description = des

    def getName(self):
        return self.item_name

    def getPrice(self):
        return self.item_price

    def getQty(self):
        return self.item_quantity

    def getDes(self):
        return self.item_description

    def print_item_cost(self):
        print(
            f'{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity * self.item_price)}')
        pass

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    pass

class ShoppingCart:
    def __init__(self, nme="none", date="January 1, 2016"):
        self.customer_name = nme
        self.current_date = date
        self.cart_items = []
        pass

    def get_num_items_in_cart(self):
        qty = 0
        for item in self.cart_items:
            qty += item.getQty()
        return qty
    def getCartName(self):
        return self.customer_name
    def getDate(self):
        return self.current_date
    def add_item(self, item):
        self.cart_items.append(item)
        pass

    def remove_item(self, name):
        match = False
        if self.get_num_items_in_cart()>0:
            for i in self.cart_items:
                if i.getName() == name:
                    self.cart_items.remove(i)
                    match = True
                # if self.cart_items[i].getName() == name:
                #     self.cart_items.remove(i)
                #     match = True
                    print()
                    return
        if not match:
            print("Item not found in cart. Nothing removed.")
        pass
        print()

    def modify_item(self, obj):
        match = False
        if self.get_num_items_in_cart() > 0:
            for i in range(len(self.cart_items)):
                if self.cart_items[i].getName() == obj.getName():
                    #print("Enter the item name:")
                    #name = input()
                    #print("Enter the item description:")
                    #des = input()
                    #print("Enter the item price:")
                    #price = float(input())
                    #print("Enter the item quantity:")
                    #qty = int(input())
                    #self.cart_items[i].setName(name)
                    #self.cart_items[i].setPrice(price)
                    self.cart_items[i].setQty(obj.getQty())
                    #self.cart_items[i].setDesc(des)
                    match = True
                    return
        if not match:
            print("Item not found in cart. Nothing modified.")
        pass
        print()

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += int((item.getQty() * item.getPrice()))
        return total_cost
        pass

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        print()

        if len(self.cart_items)>0:
            for item in self.cart_items:
                item.print_item_cost()
                pass
            print()

        if self.get_cost_of_cart() == 0:
            print("SHOPPING CART IS EMPTY")
            print()

        print(f'Total: ${self.get_cost_of_cart()}')
        print()

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        if len(self.cart_items)>0:
            print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
        pass
        print()
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
    return

if __name__ == '__main__':
    print("Enter customer's name:")
    name = input()
    print("Enter today's date:")
    date = input()
    print()
    cart = ShoppingCart(name, date)
    print(f"Customer name: {cart.getCartName()}")
    print(f"Today's date: {cart.getDate()}")

    print()

    char = ""
    while char != "q":
        print_menu()
        print("Choose an option:")
        char = input()
        while char not in ["a","q","r","c","i","o"]:
            print("Choose an option:")
            char = input()

        if char=='a':
            print("ADD ITEM TO CART")
            print("Enter the item name:")
            name = input()
            print("Enter the item description:")
            des = input()
            print("Enter the item price:")
            price = float(input())
            print("Enter the item quantity:")
            qty = int(input())
            item1 = ItemToPurchase()
            item1.setName(name)
            item1.setPrice(price)
            item1.setQty(qty)
            item1.setDesc(des)
            cart.add_item(item1)
            print()
            pass
        elif char == 'r':
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            name = input()
            cart.remove_item(name)
        elif char =='c':
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            name = input()
            print("Enter the new quantity:")
            qty = int(input())
            item = ItemToPurchase()
            item.setName(name)
            item.setQty(qty)
            cart.modify_item(item)
        elif char =='i':
            cart.print_descriptions()
        elif char =='o':
            cart.print_total()
            pass
