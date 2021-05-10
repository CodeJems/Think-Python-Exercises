# Strings

# 8-1 Learn and use string methods from the documention
'''
word = 'apple'
essay = 'Hello! \n How are you? \n I hope you are well!'
print('word'.capitalize())
print('word'.center(10,'"'))
print('word'.count('w'))
print('wording'.endswith('ing'))
print(word.find('r', 3,3)) # returns index of where letter was found
# returns  -1 if there is no char found
# print(word.index('word')) # returns ValueError when substring not found
print('123'.isalnum()) # returns true if at least one character and all are alphanumerical
print(word.isascii()) # Same above but ascii
print('123'.isdecimal()) # isdigit() same as decimale but includes extra digits
print(word.isidentifier()) # checks if used in python language
print(word.islower()) # checks if lower case
print(word.isnumeric) #Checks if number and one character
print(word.isprintable()) # true if all printable or if empty
print(word.isspace()) # if there are any spaces
print(word.istitle()) # If upper than lower case, Apple not APPLE
# print(word.issuper()) # Checks for at least 1 cased character and ALL are upper case
print(word.join('jumble')) #returns with string concatenated between each iteratable
print(word.ljust(20)) #left justified with width input
print(word.lower()) # lower case string
print(word.lstrip('pa')) # remove leading characters only, input in any order
print(word.maketrans('no','ok')) # a translation table? but not completely certain. Different uses for each amount of strings put in
print(word.partition('l')) # returns a three-tuple of the parts split by the partition input
print(word.removeprefix('ap'))
print(word.removesuffix('le'))
print(word.replace('pple','nt'))
print(word.rfind('p')) # rindex() is same, but raises valueerror
print(word.rjust(10)) # Right justified
print(word.rpartition('p')) # same as partition but starts on the right
print(word.rsplit()) # like split(), but from the right
print(word.rstrip('pe')) # like lstrip but from right
print(word.split('p')) 
print(essay.splitlines()) # can have true as input to include line breaks in line
#otherwise just returns lines of essay
print(word.swapcase()) # converts cases
print('the adventures of happy mices'.title()) # titles string similar to a book 
# gets words that shouldn't be capitalized too, not perfect
print(word.upper())
print(word.zfill(7)) # puts zeros to make a string of length input
'''
# 8-2
print('banana'.count('a'))

# 8-3
def string_slicing(a):
    b = a[::-1]
    if b==a:
        print('is palindrome')

string_slicing('tacocat')

# 8-4
#1 finds if the first char checked is lower case
#2 Always returns true
#3 returns if the last char was lower case
#4 returns true if any is lowercase
#5 returns false if any character is not lower case

# 8-5 rotate word
import string # used to generate alphabet

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
        

print(rotate_word('hello',0))