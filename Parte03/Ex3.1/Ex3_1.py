#!/usr/bin/env python3

#Imports
import argparse
import math
import time

# The second line allows for use of said functions without saying colorama.Back
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

#Global Variables

#Functions

#! camel_case
#! snakeCase      

def computeTime(value):
    time_b4 = time.time() # Seconds passed since 01/01/1970
    
    for i in range(0 , value*10**6):
        _ = math.sqrt(i)
        #print(temp)
    
    time_after = time.time()

    execution_time = time_after - time_b4
    return execution_time
    
def main():

    parser = argparse.ArgumentParser(description='Calculates the time to compute the square root of numbers up to x million')
    parser.add_argument('--max_number',type=int,metavar='',required=True,help='x')
    args=parser.parse_args()

    time_b4 = time.time()
    print(Back.RED + time.ctime(time_b4)) #ctime only converts time
    execution_time = computeTime(args.max_number)
    print("Time to compute the square root of the first " + str(args.max_number) + " was : " + str(execution_time) + " seconds.")

if __name__=='__main__':
    main()

