# 9-1 Read words.txt and prints only words with 20 or more characters

words = open('think-python-exercises/words.txt')
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
        x = x.strip()
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
    for word in words:
        word.strip()
        # print(word)
        if word == logforbid:
            continue
        for letter in word:
            # print(letter)
            if letter in forbid:
                logforbid.append(word)
                continue
    return len(logforbid)
# print(word_search_no_e(words))
print(avoid(words))


