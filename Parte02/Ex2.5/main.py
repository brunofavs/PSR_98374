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
# This function gets a list of all ASCII characters up to the pressed key, then processe's them to separate numbers from others
# The list 'inputs' has all terms in Unicode
   while True:
        key = ord(readchar.readchar())
        total_numbers=0
        total_others= 0
        inputs=[]
        other_ordered={}
        
    
          # This for loop creates a list of all UNICODE inputs
        for i in range(32,key):
            inputs.append(chr(i))
        
        index=0
        numericInput=[]
         # This for loop prints how many of that list are numbers or others and to create a dictionary with the order
        for input in inputs:
            if input.isnumeric():
                total_numbers += 1
                #numericInput.append(input)
            else:
                total_others +=1
                other_ordered[index]=input
                index += 1

        #Numeric input but with list comprehension

        numericInput=[input for input in inputs if input.isnumeric()]


        #This loop will create a numeric inputs list
        orderedInput=numericInput
        orderedInput.sort()

        print(orderedInput)
        print(other_ordered) 
        print('You entered ' + str(total_numbers) + ' numbers.')
        print('You entered ' + str(total_others) + ' others.')
        # This following lines interrupt the programm if a is pressed
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

    