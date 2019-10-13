#The function should start at the very beginning, a very good place to start
char_num = 0

#Collect the user input and return it
usr_in = input("\n\nPlease enter your text and press RETURN\n\n")
print("\nYou said:", '\n\n', usr_in, end='\n\n')

#Define the length of the phrase and return the length
char_lim = len(usr_in)
print("There are ", char_lim, " characters.", end='\n\n')

#Determine if the user wants random letters or sequential. Just checks for the
#letter "r" after making it all lowercase
function_type = input("Would you like to flip every other letter or go randomly?\n\n")
function_type = function_type.lower()
function_type = ("random" if ("r" in(function_type)) else "sequential")
print("You picked ", function_type, "\n\n")

#Define the function, which will determine if the letter index is even or odd,
# and alter the case accordingly
def SpongeBob_Letter(letter, index): #index is char_num but with makeup on
    return(letter.lower() if ((index % 2) ==0) else letter.capitalize())

#Define function for randomly altering the lowercase
def Random_Letter(letter):
    random_float = random()
    return(letter.lower() if ((random_float % 2) ==0) else letter.capitalize())
    print(random_float)
print(random_float)

#As long as the character number has not reached, then the function SpongeBob
# should return each sequential letter in order.
print("Here's your new meme:", end='\n\n')

while (char_lim != char_num, function_type = sequential):
    x = SpongeBob_Letter(usr_in[char_num], char_num) #char_num becomes index for function
    print(x, end='')
    char_num += 1

#Same While loop but for the randomized function
while (char_lim != char_num, function_type = random):
    y = Random_Letter(usr_in[char_num])
    print(y, end='')
    char_num += 1

#End the function and say goodbye
print('\n\n', end='')
print("Thanks for using my program!\n")
