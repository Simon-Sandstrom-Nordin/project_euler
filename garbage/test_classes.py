class Y:

    def __init__(self, number):
        self.counter = number

    def return_counter(self):
        return self.counter


y = Y(3)
print(y.return_counter())
