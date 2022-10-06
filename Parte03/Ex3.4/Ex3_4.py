#!/usr/bin/env python3
# Imports ---------------------------
# from collections import namedtuple


# Complex = namedtuple('Complex', ['r', 'i'])


# Functiions ---------------------------



class Complex:

    def __init__(self,r=0,i=0):
        #Default values
        self.r=r
        self.i=i

    def __str__(self):
        text= str(self.r) + ' + ' + str(self.i) + 'i'
        return text

    def addComplex(self , y):
        # add code here ...
        # returns a object

        a = self.r
        b = self.i
        c = y.r
        d = y.i

        real = a+c
        imaginary = b+d

        # Creates a new object result of the sum
        return Complex(real,imaginary)



    def multiplyComplex(self, y):
        # add code here ...
        #(a+bi)(c+di) = ac + adi + bci + bdi2

        a = self.r
        b = self.i
        c = y.r
        d = y.i

        real = a*c - b*d
        imaginary = a*d + b*c

        return Complex(real,imaginary)

# main ---------------------------

def main():
    # define two complex numbers as tuples of size two

    #? Do we have to specify the flag?

    c1 = Complex(r=0,i=5)
    c2 = Complex(-2, 7)

    # Test add
    c3 = c1.addComplex(c2)
    c4= c1.multiplyComplex(c2)

    # print(str(c1.r))
    # print(str(c1.i))
    
    print(c3)
    print(c4)
    #test multiply
    

if __name__ == '__main__':
    main()