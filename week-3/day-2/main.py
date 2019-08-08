# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# a = float(raw_input('Enter first number: '))
# b = float(raw_input('Enter second number: '))

# print max(a, b)

# def ask():
#     message = raw_input('Enter a message: ')
#     print message * 2

# ask()

# def multiply(a,b,c):
#     product = a * b * c
#     print product + 3


# a = int(raw_input('Enter first number: '))
# b = int(raw_input('Enter second number: '))
# c = int(raw_input('Enter a third number: '))

# multiply(a, b, c)

def ask():
    message = raw_input('Enter a message: ')
    while message is not "Yo what up":
        message = raw_input('Enter a message: ')

ask()