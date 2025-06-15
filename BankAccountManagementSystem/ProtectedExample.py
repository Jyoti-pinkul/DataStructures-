class A:
    def __init__(self):
        self._value = 10  # Protected

class B(A):
    def print_value(self):
        print(self._value)  # ✅ Accessible

obj = B()
print(obj._value)  # ⚠️ Technically accessible, but discouraged
