class Payment():
    def __init__(self,payment_id,order,amount,payment_method,payment_status,payment_date):
        self.payment_id=payment_id
        self.order=order
        self.amount=amount
        self.payment_method=payment_method
        self.payment_status=payment_status
        self.payment_date=payment_date
        
        
    def make_payment(self):
        self.payment_status="Success"
        
        print("Payment completed successfully.")
        
    def verify_payment(self):
        if self.payment_status == "Success":
            return True
        return False
        
    def refund(self):
        
        if self.payment_status != "success":
            print("Refund cannot be processed")
            return
        
        self.payment_status = "Refundable"
        print("Refund processed succesfully")
        
        