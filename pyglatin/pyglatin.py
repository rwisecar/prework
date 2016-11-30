pyg = 'ay'

def translate():
    original = raw_input('Please enter a word: ')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word[1:] + first + pyg
        print new_word
    again = raw_input('Would you like to try again? ')
    if again.lower() == 'y' or again.lower() == 'yes':
        translate()
    else:
        print 'Goodbye'

def run_translator():
    print 'Welcome. This is a pyglatin translator.'
    translate()

run_translator()
