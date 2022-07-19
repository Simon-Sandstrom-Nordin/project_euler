# Python has no integer overflow problem!
# as long there's free memory in the system, things are fine <3

x = 1
for k in range(1, 1000):
    x = x * 10


def fibonacci(f1, f2):
    return f1 + f2


counter = 2
f1 = 1
f2 = 1
f_temp = 0

while f2 < x:
    counter += 1
    f_temp = fibonacci(f1, f2)
    f1 = f2
    f2 = f_temp

print(counter)

# answer: index of first fibonacci number to with at least 1000
# digits is 4782
