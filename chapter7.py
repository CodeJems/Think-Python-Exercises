# Iteration

# 7-1
# Square roots with Newton's method
import math
def sqroot(a,x):
    epsilon = 0.0001
    y = (x+a/x)/2
    if abs(x-y) < epsilon:
        return y
    else:
        x = y
        return sqroot(a,x)

def test_square_root():
    print('')
    dash = '-'*42
    for x in range(10):
        if x == 0:
            print(dash, '\n{:^5s}{:^10s}{:^15s}{:^10s}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
            print(dash) 
        else:
            a=sqroot(x,x/2)
            b=math.sqrt(x)
            c=abs(sqroot(x,x/2)-math.sqrt(x))
            print('{:^5d}{:^10f}{:^15f}{:^10f}'.format(x,a,b,c),)
    print(dash)
test_square_root()

'''
old code - learned how to do columns above
# # for x in range(25):
#     sq = x
#     diff = abs(sqroot(sq,5)-math.sqrt(sq))
#     print("The square root of {0} is approximately {1:.4f} according to my function, with a diff of {2} from math.sqrt()".format(sq,sqroot(sq,5),diff))
'''
# 7-2
# repeating eval until user types 'done'

def eval_loop(done):
    while done != "done":
        evalme = input("What would you like to evaluate? ")
        print(eval(evalme))
        done = input("Type done to quit, or press enter: ")
        if done == 'done':
            return evalme
# print(eval_loop(''))

# 7-3
# Srinivasa Ramanujan 1/pi

def calculatePi(n, lastvalue):
    epsilon = 10**-323
    if n == 0:
        print('ran n=0')
        lastvalue = 2*math.sqrt(2)*1103/9801
        print(lastvalue)
        return calculatePi(n+1,lastvalue)
    elif abs(1/math.pi-lastvalue) < epsilon:
        print('found inverse pi on k = {0}, or {1} steps'.format(n,n+1))
        return 1/lastvalue
    else:
        lastvalue = lastvalue + ((2*math.sqrt(2))/9801)*((math.factorial(4*n))*(1103+26390*n))/((math.factorial(n)**4)*396**(4*n))
        print(lastvalue,n)
        return calculatePi(n+1,lastvalue)
print(calculatePi(0,0))
# Incredibly accurate inverse pi algorithim. to 10^-323 at 4 steps
        

