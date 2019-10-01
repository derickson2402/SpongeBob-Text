#The function should start at the very beginning, a very good place to start
char_num = 0

#Collect the user input and return it
usr_in = input("\n\nPlease enter your text and press RETURN\n\n")
print("\nYou said:", '\n\n', usr_in, end='\n\n')

#Define the length of the phrase and return the length
char_lim = len(usr_in)
print("There are ", char_lim, " characters.", end='\n\n')
print("Here's your new meme:", end='\n\n')

#Define the function, which will determine if the letter place is even or odd,
# and alter the case accordingly
def SpongeBob(letter, place):
    return(letter.lower() if ((place % 2) ==0) else letter.capitalize())

#As long as the character number has not reached, then the function SpongeBob
# should return each sequential letter in order.
while (char_lim != char_num):
    x = SpongeBob(usr_in[char_num], char_num)
    print(x, end='')
    char_num = (char_num+1)
print('\n\n', end='')

#End the function and say goodbye
print("Thanks for using my program!\n")
