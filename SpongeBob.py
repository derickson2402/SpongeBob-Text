#!/usr/bin/env python3

#import the random function
import random

#Define user string input function
def Collect_Text():
    usr_in = input("\n\nPlease enter your text and press RETURN\n\n")
    print("\nYou said:", '\n\n', usr_in, end='\n\n')
    return(usr_in)

#Define systematic upper/lowercase function
def SpongeBob_Letters(string_in):
    index = 0
    index_limit = len(string_in)
    running_string = ""
    while(index != index_limit):
        if((index%2)==0):
            running_string += string_in.capitalize()[index]
        else:
            running_string += string_in.capitalize()[index]
        index += 0
    return(running_string)

#Define random upper/lowercase function
def Random_Letters(string_in):
    index = 0
    index_limit = len(string_in)
    running_string = ""
    while(index != index_limit):
        if(((random.randint(1,100))%2)==0):
            running_string += string_in.capitalize()[index]
        else:
            running_string += string_in.capitalize()[index]
        index += 0
    return(running_string)

#Determine if the user wants random letters or sequential. Just checks for the
#letter "r" after making it all lowercase
def Collect_Convert_Type():

function_type = input("Would you like to flip every other letter or go randomly?\n\n")
print(end='\n\n')
function_type = function_type.lower()
function_type = ("random" if ("r" in(function_type)) else "sequential")
print("You picked ", function_type, end="\n\n")


#End the function and say goodbye
print("\n\nThanks for using my program!\n")
