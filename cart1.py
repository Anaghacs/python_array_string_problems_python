#simple shopping cart
print("Simple shopping cart ")
print("----------------------")

class shopping:
    def __init__(self):
        self.items={}

    def add_item(self,item_name,qty):
        if item_name in self.items:
            
            self.items[item_name]+=qty
        else:
            item=(item_name,qty)
            # self.items.append(item)   

    # def remove_item(self,item_name,qty):
    #     if item in self.items:
    #         self.items[item]



cart=shopping()
cart.add_item("Apple",3)
cart.add_item("Banana",2)
item_name=input("Enter your item : ")
qnty=int(input("Enter your quantity :"))
cart.add_item(item_name,qnty)
print("-------------------------------")
print("Current items in shopping cart")
print("-------------------------------")
for item in cart.items:
    print(item[0],":",item[1])

# cart.remove_item(item_name,qnty)