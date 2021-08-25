# Chapter 12 Exercises - Tuples

# Uses ch 11 answers to make a dictionary of all the words cleaned up
book = open('words.txt')
words = book.readlines()
def make_dictionary(words):
    all_words = {}
    for word in words:
        word = word.strip()
        all_words[word] = 0

    return all_words
all_words = make_dictionary(words)
## End of Ch 11 work

# sumall exercise p.143
def sumall(*innum):
    sumval = 0
    for x in innum:
        sumval = sumval + x
    return sumval
# printout of summed up list with any number of arguments using variable-length tupple assignment 
# print(sumall(1,2,3,4))

# 12-1 most_frequent to find most frequent letters in each word, and prints them in descending order of frequency
# Outputs and adds to the count of letters as they appear to a new dictionary
def most_frequent(word, d):
    for letters in word:
        if letters not in d:
            d[letters] = 1
        else:
            d[letters] = d[letters] + 1 
    return d
# Finds the amount of letters in all_words and prints them in descending order
def all_letters_frequency(words):
    d = dict()
    # For each word in the dictionary
    for word in words:
        # Count each letter
        most_frequent(word, d)
    values = []
    # For calculating total percentage
    total_sum = 0
    for x in d:
        total_sum = total_sum + d[x]
    # and split every item of the finished count into a key/value pair
    for key, value in d.items():
        percent = value/total_sum
        # and append that value and percentage of occurance to this list 
        values.append([value,key,percent])
    # Then sort that list so it goes from highest to lowest
    values.sort(reverse = True)
    # And return that sorted list
    return values

# To have solution for 12-1
# print(all_letters_frequency(all_words))        


# 12-2 - Find annagrams and print results
# tuple append, referencing a new tuple as itself. 
# see if tuple is in all_words keys

# test words 
some_words = dict()
test_words = ['deltas','lasted','alpha','beta','omega']
for x in test_words:
    some_words[x] = 0
# print(some_words)

def make_list(word):
    ordered_word = list(word)
    ordered_word.sort()
    ordered_word = ''.join(ordered_word)
    return ordered_word


def find_annagrams(words):
    d = dict()
    r = dict()
    # print(d)
    for word in words:
        ordered_letters = make_list(word)
        # print(ordered_letters)
        if ordered_letters not in d:
            d[ordered_letters] = [word]
        else:
            d[ordered_letters].append(word)
    for x in d:
        if len(d[x]) > 1:
            r[x] = d[x]
    return r

def ordered_annagrams(annagrams):
    annagrams_list = []
    for words in annagrams.values():
        annagrams_list.append((len(words), words))
    annagrams_list.sort()
    return annagrams_list

# print(find_annagrams(some_words))
# print(ordered_annagrams(find_annagrams(all_words)))
# print(d)
 
#  12-3 What collection of 8 letters forms the most possible bingos

def scrabble_bingo(annagrams):
    eight_letter_words = dict()
    letter_count = dict()
    solution = []
    for annagram, word in annagrams.items():
        if len(annagram) == 8:
            eight_letter_words[annagram] = word
        for letter in annagram:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] = letter_count[letter] + 1
    for letter, count in letter_count.items():
        solution.append((count, letter))
    solution.sort(reverse = True)

    return solution

print(scrabble_bingo(find_annagrams(all_words)))
# Printout of solution
# [(9333, 'e'), (7735, 's'), (6097, 'r'), (5475, 'a'), (5059, 'i'), (4658, 't'), (4174, 'n'), (3644, 'o'),
# (3416, 'l'), (2782, 'd'), (2321, 'c'), (1899, 'g'), (1894, 'p'), (1884, 'u'), (1653, 'm'), (1282, 'h'), 
# (1115, 'b'), (632, 'f'), (584, 'w'), (567, 'y'), (557, 'v'), (556, 'k'), (72, 'x'), (60, 'q'), (57, 'z'), (41, 'j')]