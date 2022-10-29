# Name: - Neeraj Kumar
# ID: - 2047559

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0


    def setName(self, nme):
        self.item_name = nme
    def setPrice(self, val):
        self.item_price = val
    def setQty(self, qty):
        self.item_quantity = qty
    def getName(self):
        return self.item_name
    def getPrice(self):
        return self.item_price
    def getQty(self):
        return self.item_quantity
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity*self.item_price)}')
        pass
    pass


if __name__ == '__main__':
    print("Item 1")
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    qty = int(input())
    item1 = ItemToPurchase()
    item1.setName(name)
    item1.setPrice(price)
    item1.setQty(qty)

    print()

    print("Item 2")
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    qty = int(input())
    item2 = ItemToPurchase()
    item2.setName(name)
    item2.setPrice(price)
    item2.setQty(qty)
    #output
    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print(f"Total: ${int((item1.getQty()*item1.getPrice())+(item2.getQty()*item2.getPrice()))}")
    pass
