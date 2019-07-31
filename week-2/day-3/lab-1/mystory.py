story = """
    I awoke this morning feeling {adj}.
    The {noun1} was pleasant and {adj1}.
    There was one {noun2} though,
    The {noun3}. The time was somehow 9:17 AM.
    I was meant to wake up at 6:00 AM. 
    Where did the {noun3} go?
"""

seq = ['adj', 'noun', 'adj', 'noun', 'noun']
words = []

def ask(message):
    word = raw_input(message)
    if not word:
        ask(message)
    else:
        return word

for wordType in seq:
    word = ask('Enter a ' + wordType + ': ')
    words.append(word)

if len(words) is not 5:
    print 'You need to enter an adj, noun, adj, noun, noun, and noun'

adj, noun1, adj1, noun2, noun3 = words

print story.format(
    adj = adj,
    adj1 = adj1,
    noun1 = noun1,
    noun2 = noun2,
    noun3 = noun3
)
