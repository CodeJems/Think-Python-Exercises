import math

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

# 9-5 uses all words that you put into it

def uses_all(words):
    uses = input('What letters must your words have? ')
    test={}
    good_word = []
    for x in uses:
        test[x] = False
    for word in words:
        for x in uses:
            test[x] = False
        word = word.strip()
        for letter in word:
            for x in test.keys():
                if letter == x:
                    test[x] = True
        if all(test.values()):
            good_word.append(word)
    return good_word

# print(uses_all(words))

# 9-6 abecedarian order (alphabetical order) of words

def abecedarian(words):
    uses = 'abcdefghijklmnopqrstuvwxyz'
    x = 0
    temp = ''
    good_word = []
    checkarr = []
    check = False
    for word in words:
        if temp != word:
            x = 0
            temp = word
        word = word.strip()
        for letter in word:
            if letter not in uses[x:25]:
                checkarr.append(False)
            else:
                checkarr.append(True)
                x = uses.index(letter)
        for x in checkarr:
            if x:
                check = True
                continue
            else:
                check = False
                break
        if check == True:
            good_word.append(word)
        checkarr = []
    return good_word
                
# print(abecedarian(['abc','aaaaab','acd','cba'])) 
# print(abecedarian(words))            

# Part 2 of Chapter 9

# 9-7 print words with 3 consecutive double letters 'aabbcc' counts but not 'aaibbcc'

def puzzler(word):
    i = 0
    print(word)
    while i < len(word)-1:
        if len(word) < 6:
            return False
        elif i+1 < len(word) and word[i+1] == word[i]:
            # if the next letter matches this letter
            i = i+2
            if i+1 < len(word) and word[i+1] == word[i]:
                i = i+2
                if i+1 < len(word) and word[i+1] == word[i]:
                    return True
                i = i - 2
            i = i - 2
        i = i + 1
    return False

# print(puzzler('aaliis'))

## Searches for words with function
def word_search(words):
    good_words = []
    for word in words:
        word = word.strip()
        if puzzler(word): # put function as an if statement
            good_words.append(word)
    return good_words

# print(word_search(words))

def find_digits(num):
    if num > 0:
        numdigits = math.floor(math.log10(num))+1
    elif num == 0:
        numdigits = 1
    
    return numdigits

def odo_search():
    # 6 digits, the last 4, then the last 5, then the last 6 must be palindromic as you increment by 1
    number = 0
    while number <= 999997:
        test = find_digits(number)
        if test == 6:
            return number
        number = number + 1

# b = a[::-1]
# if b==a:
#     print('is palindrome')

a = '123456'
b = a[3::-1] # [(start from nth number):(calling string before the nth number in original value):(-1 is reverse)]
print(a,' ',b)
a = '123456'
b = a[4::-1] # [(start from nth number):(calling string before the nth number in original value):(-1 is reverse)]
print(a,' ',b)
a = '123456'
b = a[5::-1] # [(start from nth number):(calling string before the nth number in original value):(-1 is reverse)]
print(a,' ',b)


# print(len(12))
# print(odo_search())


'''
# From book post chapter

def book_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def book_avoids(word, forbid):
    for letter in word:
        if letter in forbid:
            return False
    return True

def book_uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

# def book_uses_all(word, required):
#     for letter in required:
#         if letter not in word:
#             return False
#     return True

#Alternative solution using previously solved problem
def book_uses_all(word,required):
    return book_uses_only(required,word)

# Loopng with indices

def book_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True
'''