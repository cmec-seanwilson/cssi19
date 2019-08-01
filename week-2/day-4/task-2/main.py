# def characterCount(sentence):
#     return len(sentence)

# sentence = raw_input('Enter a sentence to be counted: ')
# # print (lambda sentence: len(sentence))(sentence)

def characterCount (sentence):
    occurences = {}
    for letter in sentence:
        if occurences.has_key(letter):
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    return occurences

sentence = raw_input('Enter a sentence: ')
print characterCount(sentence)