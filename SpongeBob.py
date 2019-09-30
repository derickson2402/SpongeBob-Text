#Collect the user input and define length

usr_in = input()
limit = len(usr_in)
character = 0


#Define the even/odd function

def SpongeBob():
    #Using the global variables
    global usr_in
    global limit
    global character

    #Checking for even or odd
    #I shouldn't have to define global variable again
    if ((character % 2) == 0):
        print(usr_in.lower()[character])
        character+1
    else:
        print(usr_in.capitalize()[character])
        character+1

#function SpongeBob should be defined by now
#every other letter should capitalize

while (limit != character):
    SpongeBob()
