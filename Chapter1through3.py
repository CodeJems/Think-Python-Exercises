# How many seconds in 42 minutes and 42 seconds
ans1 = 42*60+42
print('There are {0} seconds in {1}'.format(ans1,'42 minutes and 42 seconds'))
# How many miles are there in 10 kilometers? 1 mi = 1.61 km
ans2 = 10/1.61
print('There are {0:.3f} miles in {1}'.format(ans2, '10 kilometers'))
# If you run 10 km in 42 min 42 seconds what is your avg pace?
ansmeter = (10/ans1)*1000
ansmile = ans2/ans1
print('Your average speed was {0:.3f} meters per second, or {1:.5f} miles per second'.format(ansmeter,ansmile))
# What is the volume of a sphere with radius 5?
pi=3.14159
r = 5
vol = r**3*pi*4/3
print('The volume of a sphere with radius {0} is {1:.2f}'.format(r,vol))
# 24.95$ per book, book stores get a 40% discount. Shipping costs 3$ for the first copy and 0.75$ for each additional copy. What is the wholesale cost for 60 copies?
ncopies = 60
pricebook = 24.95
discount = 0.40
firstship = 3
shippingplus = 0.75
wholesale = ncopies*(24.95*discount)+(ncopies-1)*shippingplus+firstship
print('The wholesale cost of {0} books at a {1:.0f}% discount is ${2:.2f}'.format(ncopies,discount*100,wholesale))
# Easy pace = 8:15 per mile, Tempo pace = 7:12 per mile, you leave at 6:52am, when do you get home? 1 mile easy, 3 miles tempo, 1 mile easy
amtime = 0
easypace = 8*60+15
tempopace = 7*60+12
morningrunlength = 2*easypace+3*tempopace
morningtime = 6*60*60 + 52*60
combinedtime = (morningrunlength+morningtime)/60
while combinedtime/60 > 1:
    combinedtime = combinedtime-60
    amtime +=1
print('If you leave at 6:52am, you will return at {0}:{1:.0f}am'.format(amtime,combinedtime))
#print a grid shape using by making a function
def printbox(rows,columns):
    rows = rows*5
    columns = columns*5
    i = 0
    j = 0
    while i < rows+1:
        if i%5 == 0:
            if j%5 == 0:
                if j == columns:
                    print('+')
                    i+=1
                    j=0
                    continue
                else:
                    print('+', end=' ')
            else:
                print('-', end=' ')
        else:
            if j%5 == 0:
                if j == columns:
                    print('|')
                    i+=1
                    j=0
                    continue
                else:
                    print('|', end=' ')
            else:
                print(' ', end=' ')
        j+=1
printbox(2,10)


    

