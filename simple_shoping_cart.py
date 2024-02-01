class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
        print(f"{quantity} {item}{'s' if quantity > 1 else ''} added to the cart.")

    def remove_item(self, item, quantity):
        if item in self.cart:
            if quantity >= self.cart[item]:
                del self.cart[item]
            else:
                self.cart[item] -= quantity
            print(f"{quantity} {item}{'s' if quantity > 1 else ''} removed from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def view_cart(self):
        print("\nYour shopping cart:")
        for item, quantity in self.cart.items():
            print(f"{item.capitalize()}:{quantity}")

# Example usage:
cart = ShoppingCart()

cart.add_item("Apples", 3)
cart.add_item("Bananas", 2)
cart.add_item("Apples", 2)
cart.add_item("Oranges", 1)

cart.view_cart()

cart.remove_item("Bananas", 1)

cart.view_cart()
