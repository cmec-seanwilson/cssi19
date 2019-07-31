quantity = raw_input('Enter a quantity: ')

try:
    quantity = int(quantity)
    noun = raw_input('Enter a word: ')
    plural = noun + 's' if quantity > 1 else noun
    print quantity, plural
except ValueError as error:
    print 'Enter a valid integer for the quantity'