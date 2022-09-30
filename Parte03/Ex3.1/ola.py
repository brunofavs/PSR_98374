#!/usr/bin/env python3

#Imports
import argparse
import time

#Global Variables

#Functions

parser=argparse.ArgumentParser(description='Calculates the time to compute the square root of numbers up to x million')
parser.add_argument('--max_number',type=int,metavar='',required=True,help='x')
args=parser.parse_args()

def computeTime(value):
    seconds=time.time()
    print(time.ctime(seconds))


def main():
    print('ola')
    computeTime(args.max_number)

if __name__=='__main__':
    main()

