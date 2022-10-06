#!/usr/bin/env python3
# Imports ---------------------------
from collections import namedtuple




# Functiions ---------------------------

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    # add code here ...
    # returns a tuple
    # I could've unwrapped the tupple
    a=x.r
    b=x.i
    c=y.r
    d=y.i

    real=a+c
    imaginary=b+d


    return Complex(real,imaginary)



def multiplyComplex(x, y):
    # add code here ...
    # returns a tuple
    #(a+bi)(c+di) = ac + adi + bci + bdi2

    a=x.r
    b=x.i
    c=y.r
    d=y.i

    real = a*c - b*d
    imaginary = a*d + b*c

    return Complex(real,imaginary)
    


def printComplex(x):
    # add code here ...
    # returns void
    print("Your complex number is " + str(x.r) + " + " + str(x.i) + "i" )


# main ---------------------------

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 5)
    c2 = Complex(-2, 7)

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