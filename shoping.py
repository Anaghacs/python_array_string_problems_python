# print("------------------------")
# print("! Simple shopping cart !")
# print("------------------------")

# class shopping:
#     def _init_(self):
#         self.items= {}
#     def add_item(self, item_name, qty):
#         if item_name in self.items:
#             self.items[item_name] += qty
#         else:
#             self.items[item_name] = qty
#         print(f"{qty} {item_name}{'s' if qty > 1 else ''} added to the cart.")
#     def view_cart(self):
#         print("Your shopping cart:")
#         for item_name, qty in self.items.items():
#             print(f"{item_name.capitalize()}:{qty}")
# cart = shopping()
# cart.add_item("Apples", int(input("Enter the quantity of Apples to add: ")))
# cart.add_item("Bananas", int(input("Enter the quantity of Bananas to add: ")))
# cart.add_item("Apples", int(input("Enter the quantity of Apples to add: ")))
# cart.add_item("Oranges", int(input("Enter the quantity of Oranges to add: ")))

# cart.view_cart()

print("Simple shopping cart ")
print("----------------------")

class Shopping:
    def _init_(self):
        self.items = {}

    def add_item(self, item_name, qty):
        if item_name in self.items:
            self.items[item_name] += qty
        else:
            self.items[item_name] = qty

    def remove_item(self, item_name, qty):
        if item_name in self.items:
            self.items[item_name] -= qty
            if self.items[item_name] <= 0:
                del self.items[item_name]

cart = Shopping()
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
item_name = input("Enter your item: ")
qty = int(input("Enter your quantity: "))
cart.add_item(item_name, qty)

print("-------------------------------")
print("Current items in shopping cart")
print("-------------------------------")
for item, quantity in cart.items.items():
    print(item, ":", quantity)

# Example of removing an item
# cart.remove_item(item_name, qty)