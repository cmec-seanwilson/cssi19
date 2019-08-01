import math

def Factors(x):
    factors = []
    originalFactor = abs(x)
    for i in range(1, originalFactor + 1):
        if originalFactor % i == 0:
            factors.append(i)
        i += 1
    print factors

Factors(9)

# def CountToN(x):
#     try:
#         x = int(x)
#         for i in range(1, abs(x) + 1):
#             print i
#     except ValueError as error:
#         print 'Enter a valid number'

# num = raw_input('Enter a number: ')
# CountToN(num)