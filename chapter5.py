#5-1

import time
import math as m
linenum=0
info = time.gmtime()
text=[info[3],":",info[4],":",info[5]]
for line in text:
    if(len(text)-linenum==1):
        print(line)
    else:
        linenum+=1   
        print(line, end="")

#5-2

def check_fermat():
    a=int(input("What is a?"))
    b=int(input("What is b?"))
    c=int(input("What is c?"))
    n=int(input("What is n?"))
    if a**n+b**n == c**n and n > 2:
        print("Fermat was wrong!")
    elif a**n+b**n == c**n and n<=2:
        print("That is a solution!")
    else:
        print("No, that doesn't work.")

# Playing with ternary operators for fun :shrug:
# check_fermat()
# outstuff = '2'
# a=("no","yes")[outstuff=='2'] 
# print(a)
# the above tuple ternary operator is not often preferred as every element is evaluated before the value out is read.
# The <conditional> if <true> else <false> ternary is preferred for variable setting
# Below is a better use of a ternary operator so that answers are only evaluated after the conditional statement
instuff = 3
print("yes") if instuff == 4 else print("no")

#5-3

def is_triangle(a):
    if a[0] > a[1]+a[2] or a[1] > a[2]+a[0] or a[2] > a[1]+a[0]:
        print('no triangle')
    else:
        print('This can be a triangle')

def get_lengths():
    lengths = []
    lengths.append(int(input("What is the length of a?")))
    lengths.append(int(input("What is the length of b?")))
    lengths.append(int(input("What is the length of c?")))
    return lengths
is_triangle([3,4,5])
# is_triangle(get_lengths())

#5-4 
def recurse(n,s):
    if n == 0:
        print(s)
    else:
        recurse(n-1,n+s)
recurse(15,0)
# Below causes infinite recursion
# recurse(-1,0)
'''
Any value n<0 will cause infinite recurseion
'''
#Example of a docstring, can be 'x3 or "x3 for multiline comments

#5-5

import turtle

def draw(t,length,n):
    if n == 0:
        return
    angle = 60
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)
jelly = turtle.Turtle()
# draw(jelly,5,6)

#5-6 still using jelly the turtle
def drawKoch(t,length,test):
    if length<test:
        t.fd(length)
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.lt(60)
        t.fd(length)
    else:
        drawKoch(t,length/3,test)
        t.lt(60)
        drawKoch(t,length/3,test)
        t.rt(120)
        drawKoch(t,length/3,test)
        t.lt(60)
        drawKoch(t,length/3,test)

# drawKoch(jelly,20,3)
# jelly.bk(20*3)
# for x in range(20):
#     jelly.lt(360)
        
def kochSnow(t,length,test,face):
    drawKoch(t,length,test)
    t.rt(360/face)
    kochSnow(t,length,test,face)
    

kochSnow(jelly,40,10,6)
