#!/usr/bin/env python3

#Imports

import readchar

#Global Variables

# Programm

#chr() converts ASCII to Unicode
#ord() converts Unicode to ASCII 
#is unicode 'normal text'?


def printAllCharsUpTo():
    #The functions prints all char's from space(ASCII 0d32) to the input
    key = ord(readchar.readchar())
    
    for i in range(32,key):
        print(chr(i))

    return 

def readAllUpTo():

    while True:
        key = ord(readchar.readchar())
    
        for i in range(32,key):
            print(chr(i))
        
        temp=readchar.readkey()
        if temp == "a":
            break

    return 

    
def countNumbersUpTo():

   while True:
        key = ord(readchar.readchar())
        total_numbers=0
        total_others= 0
    
        for i in range(32,key):
            #print(str(chr(i).isnumeric))
            if chr(i).isnumeric():
                total_numbers += 1
            else:
                total_others +=1

        print('You entered ' + str(total_numbers) + ' numbers.')
        print('You entered ' + str(total_others) + ' others.')
        
        # This following lines interrupt the programm if a is pressed, however this requires you to click twice
        temp=readchar.readkey()
        if temp == "a":
            break 


def main():
    #printAllCharsUpTo()
    #readAllUpTo()
    countNumbersUpTo()
    return

if __name__== '__main__':
    main()

    