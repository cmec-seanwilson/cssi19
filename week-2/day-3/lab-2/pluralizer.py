quantity = raw_input('Enter a quantity: ')

def pluralize(quantity, word):
    word = word.strip()
    if quantity is 1:
        return word

    rules = {
        'ife': 'ives',
        'sh': 'shes',
        'ch': 'ches',
        'us': 'i',
        'y': 'ies'
    }

    for ending in rules.keys():
        # is doesn't work here for some reason? ask
        if ending == word[-len(ending):]:
            root = word[:-len(ending)]
            return root + rules[ending]

    return word + 's'

try:
    quantity = int(quantity)
    noun = raw_input('Enter a word: ')
    print pluralize(quantity, noun)
    # plural = noun + 's' if quantity > 1 else noun
    # print quantity, plural
except ValueError as error:
    print 'Enter a valid integer for the quantity'