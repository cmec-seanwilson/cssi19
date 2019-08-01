import math

def Factors(x):
    factors = []
    originalFactor = abs(x)
    for i in range(1, originalFactor):
        if originalFactor % i == 0:
            factors.append(i)
        i += 1
    print factors

# def CountToN(x):
#     for i in range(0, abs(x) * 1):
#         print i

# CountToN(15)