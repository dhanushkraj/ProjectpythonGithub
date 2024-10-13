# name = input("What is your name? ")
# print("hello,",name)

# print functionality as per python documentation
# print(*objects, sep = " ", end = "\n", file = sys.stdout, flush = False)

# End --
# print("hello, ", end = "???")
# print(name)

# Seperator --
# print("hello,", name, sep = "???")

# Parameters --
# Types -
# Normal parameters
# Named parameters        -- As above example sep, end are called named prameters[Optional parameters].

# print("hello, "friend"")
# print('hello, "friend"')
# print("hello, \"friend\"")


# name = input("What is your name? ")

# name = name.strip()          # Removes white spaces from the input.
# print(f"hello, {name}")

# name = name.strip()
# name = name.capitalize()
# name = name.title()

# name = name.strip().title()

# name = input("What is your name? ").strip().title()
# first, last = name.split()
#
# print(f"hello, {first}")

# int --
# x = input("What's x? ")          # input - makes the value as str
# y = input("What's y? ")
#
# z = int(x) + int(y)
# print(z)

# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# print(x + y)

# print(int(input("What's x? ")) + int(input("What's y? ")))

# Float --

# round(number[, ndigits])

# x = float(input("What's x?"))
# y = float(input("What's y?"))
# z = round(x + y)
#
# print(f"{z:,}")           # To add ,(commas) for values i.e., decimal points 1,000.

# x = float(input("What's x?"))
# y = float(input("What's y?"))
# z = round(x / y)
#
# print(z)

# x = float(input("What's x?"))
# y = float(input("What's y?"))
# z = x / y
#
# print(f"{z:.3f}")

# Functions --

# def hello():
#     print('hello')
#
# name = input("What's your name?")
# hello()
# print(name)

# def hello(to = "world"):
#     print("hello,", to)
#
# hello()
# name = input("What's your name?")
# hello(name)


# def main():
#     name = input("What's your name? ")
#     hello(name)
#
# def hello(to = "world"):
#     print("hello,", to)
#
# main()

# def main():
#      x = int(input("What's x? "))
#      print("x squared is", square(x))
#
# def square(n):
#     # return n * n
#     # return n ** 2
#     return pow(n, 2)
#
# main()



















































