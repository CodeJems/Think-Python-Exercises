book = open('think-python-exercises/words.txt')
words = book.readlines()



def make_dictionary(words):
    all_words = {}
    for word in words:
        word = word.strip()
        all_words[word] = 0

    return all_words

all_words = make_dictionary(words)
# print(make_dictionary(words))

def in_dict(isword):
    global all_words
    if isword in all_words:
        return True
    return False

print(in_dict('world'))

