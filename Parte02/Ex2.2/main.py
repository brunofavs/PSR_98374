#!/usr/bin/env python3

from my_functions import *

#Global variables
maximum_value=100

def main():
    print('Starting to compute all perfect numbers up to '+str(maximum_value))

    for number in range(1,maximum_value):
     dividerList= dividers(number)
     #print(dividerList)

     if isPerfect(number,dividerList):
         print('Number '+ str(number)+ ' is perfect')
         #print(dividerList)
    else:
         print('Number '+ str(number)+ ' is not perfect')


if __name__=='__main__':
    main()

