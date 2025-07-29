import pdb
# For using pdb:
# Run this script normally using python command. Add a breakpoint() call where you want to pause execution.
# Note: you can also use an IDE's debugger tools and get a more visual experience.
# Some commands:
# n - step over
# s - step into
# q - quit
# l - list source code region
# b <int> - set breakpoint at <int> line
# w - show stack trace
# c - continue program execution until next breakpoint

# List comprehension
my_ints: list[int] = [x for x in range(4, 104)]

n: int = 100
my_fibonacci: list[int] = [0, 1]
[my_fibonacci.append(my_fibonacci[i] + my_fibonacci[i + 1]) for i in range(n - 2)]

print(my_fibonacci)

# List generators
def my_generated_ints(n: int):
    for i in range(n):
        yield i

generated_ints = my_generated_ints(10)
for i in generated_ints:
    print(i, end=", ")
print()


def my_generated_fib(n: int):
    i, j = 0, 1
    k = 0
    for l in range(n):
        if l > 1:
            k = i + j
            i = j
            j = k
            yield k
        elif l < 2:
            yield l

generated_fib = my_generated_fib(100)
for i in generated_fib:
    print(i, end=", ")
print()


def my_infinite_fib():
    i, j = 0, 1
    k = 0
    l = 0
    while True:
        if l > 1:
            k = i + j
            i = j
            j = k
            yield k
        elif l < 2:
            yield l
        l += 1

infinite_fib = my_infinite_fib()
for i in range(20):
    # breakpoint() # uncomment this line to use pdb to breakpoint here
    print(next(infinite_fib), end=", ")
print()