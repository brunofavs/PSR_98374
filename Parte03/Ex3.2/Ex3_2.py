#!/usr/bin/env python3
# Imports ---------------------------



# Functiions ---------------------------

def addComplex(x, y):
    # add code here ...
    # returns a tuple
    # I could've unwrapped the tupple

    sum=(x[0]+y[0] , x[1]+y[1])
    return sum



def multiplyComplex(x, y):
    # add code here ...
    # returns a tuple
    #(a+bi)(c+di) = ac + adi + bci + bdi2

    a,b = x
    c,d = y

    real = a*c - b*d
    imaginary = a*d + b*c

    return (real,imaginary)
    


def printComplex(x):
    # add code here ...
    # returns void
    print("Your complex number is " + str(x[0]) + " + " + str(x[1]) + "i" )


# main ---------------------------

def main():
    # define two complex numbers as tuples of size two
    c1 = (5, 5)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    c4= multiplyComplex(c1,c2)

    printComplex(c1)
    printComplex(c2)
    printComplex(c3)
    printComplex(c4)
    # test multiply
    

if __name__ == '__main__':
    main()