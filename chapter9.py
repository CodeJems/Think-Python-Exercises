# 9-1 Read words.txt and prints only words with 20 or more characters

book = open('think-python-exercises/words.txt')
words = book.readlines()
# def word_search(words):
#     good_book = []
#     for x in words:
#         x = x.strip()
#         if len(x) > 19:
#             good_book.append(x)
#     return good_book
# print(word_search(words))

# 9-2 has no e, then percentage of words that have e's in them

def has_no_e(words):
    for x in words:
        if x == 'e':
            return False
    return True

def word_search_no_e(words):
    good_book = []
    totalwords = []
    for x in words:
        x.strip()
        totalwords.append(x)
        if has_no_e(x) == True:
            # print(x)
            good_book.append(x)
    # return (len(good_book)/len(totalwords))*100
    return len(totalwords)

# print('{:.2f}%'.format(word_search_no_e(words)))

# 9-3
# Write a function that avoids a string of forbidden letters
# Then add the ability for the user to type an input string for the forbidden letters

def avoid(words):
    forbid = str(input('What letters would you like to forbid?: '))
    logforbid = []
    totalwords = []
    for word in words:
        word = word.strip()
        totalwords.append(word)
        for letter in word:
            if letter in forbid and word :
                logforbid.append(word)
                break
    return 100*len(logforbid)/len(totalwords)
# print('{:.2f}% of all words are blocked by those letters'.format(avoid(words))) 

# 9-4 uses_only - returns true if word contains only letters prompted

def uses_only(words):
    uses = input('What letters must your words have? ')
    good_word = []
    for word in words:
        word = word.strip()
        nouse = True
        for letter in word:
            if letter not in uses:
                nouse = False
        if nouse == True:
            good_word.append(word)
    return good_word
        
# print(uses_only(words))

# 9-5 Write a function named uses_all that takes a word and a string of required letters,
#and that returns True if the word uses all the required letters at least once. How many
#words are there that use all the vowels aeiou? How about aeiouy?

def uses_all(words):
    uses = input('What letters must your words have? ')
    good_word = []
    for word in words:
        word = word.strip()
        nouse = True
        for letter in word:
            if letter not in uses:
                nouse = False
        if nouse == True:
            good_word.append(word)
    return good_word