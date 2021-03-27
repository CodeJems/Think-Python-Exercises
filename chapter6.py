#Chapter 6
#6-2
def ack(m,n):
    if m == 0:
        return n+1
    elif m>=n:
        print('Infinite recursion')    
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))
    else:
        print('Undefined')

# print(ack(4,3))

#6-3 palindrome
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if word != word.lower():
        word = word.lower()
    if first(word) == last(word):
        if len(middle(word)) > 1:
            return is_palindrome(middle(word))
        else:
            return True
    else:
        return False
# print(is_palindrome('tAcOcat'))
# print(is_palindrome('putty'))

#6-4
# A number, a, is a power of b if it is divisble by b AND a/b is a power of b.
def is_power(a,b):
    if (a/b)%b == 0 and a%b == 0:
        return True 
    else:
        return False
# print(is_power(27,3))
# print(is_power(4,2))
# print(is_power(9,3))

#6-5
# GCD -- if b == 0 then GCD(a,b) = a
# if r is the remainder when a/b then gcd(a,b) == gcd(b,r)
def gcd(a,b):
    if b > a: # make a biggest value
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    elif b%a != 0:
        r = a%b
        return gcd(b,r)
    else:
        return b
print(gcd(371,2457))