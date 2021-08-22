book = open('words.txt')
words = book.readlines()


# 11-1 problem
def make_dictionary(words):
    all_words = {}
    for word in words:
        word = word.strip()
        all_words[word] = 0

    return all_words

all_words = make_dictionary(words)
# print(all_words)

def in_dict(isword):
    global all_words
    if isword in all_words:
        return True
    return False

# print(in_dict('word'))

# Fibonacci Dict Example P#132
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        # print(known)
        return known[n]
    
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
# Printing solutions for any size of fibonacci values. Limit is much larger than the list version
def printfibo(invalue):
    n=0
    while(n<invalue):
        print(n, ':',fibonacci(n))
        if n>invalue:
            break
        n=n+1

# printfibo(10000)

# 11-2 use method setdefault to write invert dict more concisely

def invert_dict(indict):
    inverted_dict = {}
    for key in indict:
        inverted_dict.setdefault(indict[key],[]).append(key)
    return inverted_dict

# Print Solution for 11-2
# # Print values
# print(invert_dict(all_words))
# # Print key(s)
# for key in invert_dict(all_words):
#         print('key: ', key)

# 11-3 Check memoization for Ackermann function (6-2)
# Making a tuple variable for the dict keys
# Tuples are immutable and can store two values so we can use them for memoization
# # Previous Ackerman function from 6-2
# def ack(m,n):
#     if m == 0:
#         return n+1   
#     elif m > 0 and n == 0:
#         return ack(m-1,1)
#     elif m > 0 and n > 0:
#         return ack(m-1,ack(m,n-1))
#     else:
#         print('Undefined')

cache = {}
def ackermann(m, n):
    # Sums all expansions
    if m == 0:
        return n+1
    # Expands a single branch
    if n == 0:
        return ackermann(m-1, 1)
    # If expansion is already memoized 
    if (m, n) in cache:
        return cache[m, n]
    else:
        # Adds to value to expansion dictionary - memoization
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]
# In this exercise the solution required tuples, which are in the next chapter. We create tuple keys of m, n for each item in the cache dictionary
# Seems to break even faster now
# print(ackermann(4,1))
# print(ackermann(3, 6))


# 11-4 
# compare a list to the dictionary keys to see if there are duplicates
def compare_duplicates(listin, comparedict):
    for key in listin:
        if key in comparedict:
            print(key)
            return True
    return False

dictin = ['wom','azkc','zzzzz']

# print(has_duplicates(all_words, all_words))
# compared list to another list -- didn't find duplicates -- redo comparing a single list to itself to find if it has any duplicates

def has_duplicates(listin):
    # Creates empty dictionary
    d = {} 
    # 
    for key in listin:
        if key in d:
            return True
        d[key] = None
    return False

# print(has_duplicates(['a','a'])) 

# 11-5 find all 'rotate pairs' in a list. To rotate a word take every letter and progress is x times through the alphabet. 
# abc rotated once is bcd

# My solution for 8-5 - Rotate Word - needs string library
import string
def rotate_word(word,num):
    code = [] # encoded alphabet
    cryptic =[] # encoded word
    alphabet = string.ascii_lowercase # generate alphabet
    num = num%26
    for x in alphabet: #creates cipher from one to the other
        value = num + alphabet.find(x)   #returns index within alphabet
        code.append(alphabet[value%26])
    for x in word:
        cryptic.append(code[alphabet.find(x)])
    return ''.join(cryptic)

# print(rotate_word('a',25))
# Now use rotate_word() to find pairs
def rotate_pairs(words):
    # Store all rotate pairs in this dict
    rotatepair = {}
    for x in words:
        # for every word in the input
        num = 1
        print(x)
        # rotate all letters through the whole alphabet
        while num < 26:
            checkval = rotate_word(x,num)
            # print(checkval)
            # Searches if the checkval exists in words
            if checkval in words:
                # creates a new item if checkval isn't in rotatepair yet
                if x not in rotatepair:
                    rotatepair[x] = [checkval + ' ' + str(num)]
                # Appends to list so we can see all rotated pairs of this word
                else:
                    rotatepair[x].append(checkval + ' ' + str(num))
            # iterates through all letters
            num = num + 1
    return rotatepair
# Print all pairs and the amount of rotations needed to reach that rotated pair
print(rotate_pairs(all_words))