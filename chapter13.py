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

# 13-1
# Write a program that reads a file
# Breaks each line into words
# Strips Whitespace and punctuation
# Converts them to lower case

# Use string methods to have punctuation and whitespace things
import string

def reader(files):
    # Read file and split into lines
    f = open(files)
    lines = f.readlines()

    word_list = []
    book = []
    # Read each line and strip white space, 
    # then create a list of all the words in that line
    for line in lines:
        line = line.strip()
        if line == "*** START OF THIS PROJECT GUTENBERG EBOOK YOUTH ***":
            word_list.clear()
        if line == "*** END OF THIS PROJECT GUTENBERG EBOOK YOUTH ***":
            break 
        line_list = line.split()
        for word in line_list:
            word_list.append(word)
    # Modify each word in the new list to remove punctuation
    # And remove empty strings and make the word lowercase
    # Then append each word to a final list of all accumulated words
    for word in word_list:
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter,"")
        word = word.lower()
        book.append(word)
    book.remove('')
        
    return book

# print(reader('test.txt'))

# 13-2
# Take the function written above and take a book from gutenberg press
# and analyze words within it

# print(reader('Youth Asimov.txt'))

def count_words(wordlist):
    memory = dict()
    # memory['total count'] = 0
    for word in wordlist:
        if word not in memory:
            memory[word] = 1
        else:
            memory[word] = memory[word]+1
        # memory['total count'] = memory['total count'] + 1
    return memory

# print(count_words(reader('Youth Asimov.txt')))

# 13-3 Find the 20 most frequent words
# 
# Use this in the function to make simpler
# print(count_words(reader('Youth Asimov.txt')))

def most_frequent(book):
    words = count_words(reader(book))
    rev_words = []
    for key, value in words.items():
        if key == 'total count':
            continue
        else:
            rev_words.append((value, key))
    rev_words.sort(reverse=True)    
        # if value not in rev_words:
        #     rev_words[value] = key
        # else:
        #     print(value, ' ', key)
            
        #     # rev_words[value].append(key)
    return rev_words[0:20]

    # return words

# print(most_frequent('Youth Asimov.txt'))

# 13-4 modify previous code to read the full word list and see how 
# many words are in the book that are not in the total word list

def out_words(list_in, list_compare):
    # process word list and create dictionary of input book
    words = count_words(reader(list_in))
    new_words = dict()
    # compare each word to the list and return
    for word, value in words.items():
        if word not in list_compare:
            new_words[word] = value
    return new_words

# print(out_words('Youth Asimov.txt',all_words))

# 13-5 choose_from_hist chooses a random int from a historgram according to it's probability
# Use random module
import random

def choose_from_hist(histogram):
    probability = []
    # For each item in the historgram save it's key and value
    for key, value in histogram.items():
        # make a temporary value
        temp_value = value
        # and count through it that many times
        while temp_value > 0:
            # adding that amount to the key
            probability.append(key)
            temp_value -= 1
    # And then choose one of the values from the list
    choice = random.choice(probability)
    # and return the choice
    return choice

# print(choose_from_hist(out_words('Youth Asimov.txt',all_words)))

# 13-7 Algorithm
# Use keys to get a list of the words in the book
# Create a list that contains each value leading to the cumulative sum n
# Choose a random number 1 to n, then use a bisection search to find the index of the number you chose
        # I don't understand this assignment?
# Use the index to find the corresponding word in the list


def list_and_sum(book_words):
    wordlist = []
    wordsum = []
    total_freq = 0
    for word, freq in book_words.items():
        wordlist.append(word)
        total_freq += freq
        wordsum.append(total_freq)
    
    return wordlist

print(list_and_sum(out_words('Youth Asimov.txt',all_words)))
