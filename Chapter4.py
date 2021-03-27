import turtle
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.rt(90)
    turtle.mainloop()
# square(bob,2000)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.rt(360/n)
    turtle.mainloop()
# polygon(bob,20,20)

def circle(t,r):
    length = 3.14*r/20
    for i in range(20):
        t.fd(length)
        t.rt(360/20)
    turtle.mainloop()
# circle(bob,200)

def arc(t,r,angle):
    length = 3.14*r/360
    for i in range(angle):
        t.fd(length)
        t.rt(1)
    t.rt(90)
    t.fd(r/2)
    t.rt(180-angle)
    t.fd(r/2)
    turtle.mainloop()
arc(bob,200,150)
