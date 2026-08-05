class Product:

    def __init__(
        self,
        id,
        name,
        brand,
        category,
        description,
        price,
        stock,
        variant,
        rating,
        reviews,
        delivery_days,
        return_days
    ):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.description = description
        self.price = price
        self.stock = stock
        self.variant = variant
        self.rating = rating
        self.reviews = reviews
        self.delivery_days = delivery_days
        self.return_days = return_days
        self.discount = 0

    def display_details(self):

        print("\n========== PRODUCT DETAILS ==========\n")

        print(f"Product ID      : {self.id}")
        print(f"Product Name    : {self.name}")
        print(f"Brand           : {self.brand}")
        print(f"Category        : {self.category}")
        print(f"Description     : {self.description}")
        print(f"Price           : ₹{self.calculate_price()}")
        print(f"Stock           : {self.stock}")
        print(f"Variant         : {self.variant}")
        print(f"Rating          : {self.rating}")
        print(f"Reviews         : {self.reviews}")
        print(f"Delivery        : {self.delivery_days}")
        print(f"Return Policy   : {self.return_days}")

        print("\n=====================================")

    def check_stock(self, quantity):

        if self.stock >= quantity:
            return True

        return False

    def decrease_stock(self, quantity):

        self.stock -= quantity

        print("Stock decreased successfully.")
        print(f"Current Stock : {self.stock}")

    def increase_stock(self, quantity):

        self.stock += quantity

        print("Stock increased successfully.")
        print(f"Current Stock : {self.stock}")

    def apply_discount(self, discount_percentage):

        self.discount = discount_percentage

        print(f"Discount of {discount_percentage}% applied successfully.")

    def calculate_price(self):

        discount_amount = (self.price * self.discount) / 100

        final_price = self.price - discount_amount

        return final_price