#!/usr/bin/env python3

from my_functions import *
import argparse

#Global variables

parser = argparse.ArgumentParser(description='Computes the perfect numbers up to x') # descrição do programa once help is called
parser.add_argument('--max_number',type=int,metavar='',required=True,help='x') #optional required argument
#o contrário de optional aqui é positional, que não requer flag mas requer ordem caso haja mais argumentos
args = parser.parse_args() #passa os argumentos para um objeto chamado args

maximum_value=args.max_number

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

