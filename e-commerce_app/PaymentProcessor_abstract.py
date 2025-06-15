"""
Abstract Class: A class that cannot be instantiated and may contain abstract method
 (methods without implementation).
Abstract Method: A method that must be implemented in any subclass.
We use them to define a common interface or blueprint for a group of classes.
"""
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating via OTP...")

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(PaymentProcessor):
    def authenticate(self):
        print("Logging into PayPal...")

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

def process_payment(payment_method: PaymentProcessor, amount: float):
    payment_method.authenticate()
    payment_method.pay(amount)

# Example usage
payment1 = CreditCardPayment()
process_payment(payment1, 1000)

payment2 = PayPalPayment()
process_payment(payment2, 500)
