class Cart:

    def __init__(self, customer):

        self.customer = customer
        self.products = []
        self.subtotal = 0

    def add_product(self, product, quantity):

        if not product.check_stock(quantity):
            print("Insufficient stock.")
            return

        for item in self.products:

            if item["product"] == product:

                item["quantity"] += quantity

                print("Product quantity updated successfully.")
                return

        self.products.append(
            {
                "product": product,
                "quantity": quantity
            }
        )

        print("Product added to cart successfully.")

    def remove_product(self, product):

        for item in self.products:

            if item["product"] == product:

                item["quantity"] -= 1

                if item["quantity"] == 0:
                    self.products.remove(item)

                print("Product quantity updated successfully.")
                return

        print("Product not found in cart.")

    def update_quantity(self, product, quantity):

        if not product.check_stock(quantity):
            print("Insufficient stock.")
            return

        for item in self.products:

            if item["product"] == product:

                item["quantity"] = quantity

                print("Quantity updated successfully.")
                return

        print("Product not found in cart.")

    def view_cart(self):

        if len(self.products) == 0:
            print("Cart is empty.")
            return

        print("\n========== YOUR CART ==========\n")

        for item in self.products:

            product = item["product"]
            quantity = item["quantity"]

            print(f"Product   : {product.name}")
            print(f"Price     : ₹{product.calculate_price()}")
            print(f"Quantity  : {quantity}")
            print(f"Total     : ₹{product.calculate_price() * quantity}")
            print("--------------------------------")

        print(f"\nCart Total : ₹{self.calculate_total()}")

    def calculate_total(self):

        total = 0

        for item in self.products:

            product = item["product"]
            quantity = item["quantity"]

            total += product.calculate_price() * quantity

        self.subtotal = total

        return total

    def clear_cart(self):

        self.products.clear()
        self.subtotal = 0

        print("Cart cleared successfully.")