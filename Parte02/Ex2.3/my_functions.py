#!/usr/bin/env python3

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
