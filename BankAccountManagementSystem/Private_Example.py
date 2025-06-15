class A:
    def __init__(self):
        self.__secret = 42  # Private

    def get_secret(self):
        return self.__secret

a = A()
print(a.get_secret())     # ✅ OK
# print(a.__secret)       # ❌ AttributeError
print(a._A__secret)       # 😬 Works via name mangling (not recommended)
