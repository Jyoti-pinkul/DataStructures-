"""
Polymorphism means "many forms". In Python (and OOP),
it allows objects of different classes to be treated using the same interface
"""

class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using credit card.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)

process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
#process_payment(Payment(), 500)
