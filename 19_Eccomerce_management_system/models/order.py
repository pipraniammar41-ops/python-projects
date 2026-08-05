class Order:

    def __init__(
        self,
        order_id,
        customer,
        products,
        address,
        total_amount,
        payment,
        order_status,
        order_date,
        delivery_date
    ):

        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.address = address
        self.total_amount = total_amount
        self.payment = payment
        self.order_status = order_status
        self.order_date = order_date
        self.delivery_date = delivery_date

    def place_order(self):

        if len(self.products) == 0:
            print("Cart is empty.")
            return

        for item in self.products:

            product = item["product"]
            quantity = item["quantity"]

            product.decrease_stock(quantity)

        self.order_status = "Placed"

        print("Order placed successfully.")

    def cancel_order(self):

        if self.order_status == "Cancelled":

            print("Order is already cancelled.")
            return

        for item in self.products:

            product = item["product"]
            quantity = item["quantity"]

            product.increase_stock(quantity)

        self.order_status = "Cancelled"

        print("Order cancelled successfully.")

    def track_order(self):

        print("\n========== TRACK ORDER ==========\n")

        print(f"Order ID       : {self.order_id}")
        print(f"Customer       : {self.customer.name}")
        print(f"Order Status   : {self.order_status}")
        print(f"Order Date     : {self.order_date}")
        print(f"Delivery Date  : {self.delivery_date}")

        print("\n===============================")

    def update_status(self, status):

        valid_status = [
            "Placed",
            "Confirmed",
            "Packed",
            "Shipped",
            "Out For Delivery",
            "Delivered",
            "Cancelled"
        ]

        if status not in valid_status:
            print("Invalid order status.")
            return

        self.order_status = status

        print(f"Order status updated to '{status}'.")

    def view_order_details(self):

        print("\n========== ORDER DETAILS ==========\n")

        print(f"Order ID       : {self.order_id}")
        print(f"Customer       : {self.customer.name}")
        print(f"Order Status   : {self.order_status}")

        print("\n---------- PRODUCTS ----------")

        for item in self.products:

            product = item["product"]
            quantity = item["quantity"]

            print(f"Product  : {product.name}")
            print(f"Price    : ₹{product.calculate_price()}")
            print(f"Quantity : {quantity}")
            print(f"Total    : ₹{product.calculate_price() * quantity}")
            print("-------------------------------")

        print(f"\nTotal Amount    : ₹{self.total_amount}")
        print(f"Payment Status  : {self.payment.payment_status}")
        print(f"Shipping Address: {self.address}")
        print(f"Order Date      : {self.order_date}")
        print(f"Delivery Date   : {self.delivery_date}")

        print("\n==================================")