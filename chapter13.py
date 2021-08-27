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

print(reader('test.txt'))

# 13-2
# Take the function written above and take a book from gutenberg press
# and analyze words within it
