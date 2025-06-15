"""
We want to expose only necessary information (e.g., balance) and
hide sensitive/internal data like PIN or account activity logs.

Although Python doesn’t have strict access control like Java or C++, it follows conventions:

Access     Type	Syntax	Meaning	                                Accessible From
Public	   self.var	    No restriction	                        Anywhere
Protected	_self.var	Meant for internal use	                Class and subclass
Private	    __self.var	Stronger hiding (name mangling)	        Class only (not even subclass directly)
"""
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner              # public
        self._balance = balance         # protected
        self.__pin = pin                # private
        self.__transactions = []        # private

    def deposit(self, amount):
        self._balance += amount
        self.__transactions.append(f"Deposited ₹{amount}")
        print(f"Deposited ₹{amount} to {self.owner}'s account.")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("❌ Incorrect PIN!")
            return
        if amount > self._balance:
            print("❌ Insufficient funds.")
            return
        self._balance -= amount
        self.__transactions.append(f"Withdrew ₹{amount}")
        print(f"Withdrew ₹{amount} from {self.owner}'s account.")

    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance
        else:
            print("❌ Invalid PIN!")
            return None

    def _show_protected_data(self):
        print("🔐 Protected Data Accessed.")

    def __show_private_logs(self):  # Private method
        for t in self.__transactions:
            print(t)

    def my_pin(self, your_name):
        if your_name == self.owner:
            print("Your password is ****")
            return self.__pin
        else:
            print(f"Hi {your_name} , Your Account does not exist in our BANK !!!")


acc = BankAccount("Jyoti", 5000, 1234)

acc.deposit(2000)
acc.withdraw(1000, 1234)

print(acc.owner)             # ✅ Public: accessible
print(acc._balance)          # ⚠️ Protected: accessible, but not recommended
print(acc.get_balance(1234)) # ✅ With proper PIN

print(acc.my_pin("Jyoti"))


# ✅ Correct way to access private (name mangled)
print(acc._BankAccount__pin)                     # 1234
acc._BankAccount__show_private_logs()            # See logs


# ❌ Trying to access private attributes directly
#print(acc.__pin)             # ❌ AttributeError
#acc.__show_private_logs()    # ❌ AttributeError