#!/usr/bin/env python3

#Global variables
maximum_value=100

def dividers(value):
    #This function takes the integer input and returns all of its dividers
    # in = int ; out= list
    listDividers=[]
    for number in range(1,value):
        if value%number==0:
            listDividers.append(number)
    return listDividers

    
def isPerfect(value,dividers):
    #This function takes all the dividers and checks whether it's sum is equal to the input value.
    # in = int,list ; out = bool
    soma = 0
    for divider in dividers:
        soma = soma + divider

    if value == soma:
        return True # If the number is perfect, returns True and jumps out of the function
    return False

def main():
    print('Starting to compute all perfect numbers up to '+str(maximum_value))

    for number in range(1,maximum_value):
     dividerList= dividers(number)
     #print(dividerList)

     if isPerfect(number,dividerList):
         print('Number '+ str(number)+ ' is perfect')
         #print(dividerList)
    #  else:
    #      print('Number '+ str(number)+ ' is not perfect')


if __name__=='__main__':
    main()

