class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b


calculator = Calculator()

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = calculator.add(a, b)
print(c)
