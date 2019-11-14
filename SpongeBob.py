#!/usr/bin/env python3

#import the random function
import random

#Define systematic upper/lowercase function
def SpongeBob_Letters(string_in):
    index = 0
    index_limit = len(string_in)
    running_string = ""
    while(index != index_limit):
        temp_letter = string_in[index]
        if (index%2) == 0:
            running_string += temp_letter.lower()
        elif (index%2) == 1:
            running_string += temp_letter.capitalize()
        index += 1
    return(running_string)

#Define random upper/lowercase function
def Random_Letters(string_in):
    index = 0
    index_limit = len(string_in)
    running_string = ""
    while(index != index_limit):
        temp_letter = string_in[index]
        temp_integer = random.randint(1,100)
        if (temp_integer%2) == 0:
            running_string += temp_letter.capitalize()
        elif (temp_integer%2) == 1:
            running_string += temp_letter.lower()
        index += 1
    return(running_string)

running = True
while (running == True):
    #Collect the string from the user
    usr_in = input("\n\nPlease enter your text and press RETURN\n\n")
    print("\nYou said:", '\n\n', usr_in, end='\n\n')

    #Determine if the user wants random letters or sequential. Just checks for the
    #letter "r" after making it all lowercase
    function_type = input("Would you like to flip every other letter sequentially or go randomly?\n\n")
    function_type = ("random" if ("r" in(function_type.lower())) else "sequential")
    print("\nYou picked", function_type, end="\n\n")

    #Return the new string based upon their choice
    if(function_type == "sequential"):
        print("Here's your new meme!\n\n", SpongeBob_Letters(usr_in), end='\n\n')
    elif(function_type == "random"):
        print("Here's your new meme!\n\n", Random_Letters(usr_in), sep='', end='\n\n')
    else:
        print("There was an error processing your function type, the program will now quit.")
        running = False
        break

    #Control the state of the program
    Ask_Status = input("Do you want to make another meme? Y or N\n\n")
    if ("y" in Ask_Status.lower()):
        running = True
    elif ("n" in Ask_Status.lower()):
        running = False
    else:
        running = False
        print("There was an error processing your status, the program will now quit")

#End the function and say goodbye
print("\nThanks for using my program!\n")
