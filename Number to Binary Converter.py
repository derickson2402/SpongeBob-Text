#!/home/derickson/Projects/SpongeBob/Number\ to\ Binary\ Converter.py

def Which_Conversion(conv_type_in):
    status = "incomplete"
    while (status == "incomplete"):
        status = "complete"
        if ("1" in(conv_type_in.lower())):
            return("BtD")
        elif ("binary to decimal" in(conv_type_in.lower())):
            return("BtD")
        elif ("2" in(conv_type_in)):
            return("DtB")
        elif ("decimal to binary" in(conv_type_in.lower())):
            return("DtB")
        elif ("no" in(conv_type_in.lower())):
            exit("\nWow, fine then I guess\n")
        else:
            conv_type_in = input("A whoopsie occured. Try again.\n\n")
            status = "incomplete"
    print(end= '\n\n')

def Alpha_Check(string):
    if("a" in(string.lower()) or "b" in(string.lower()) or "c" in(string.lower()) or "d" in(string.lower())):
        return("true")
    elif("e" in(string.lower()) or "f" in(string.lower()) or "g" in(string.lower()) or "h" in(string.lower())):
        return("true")
    elif("i" in(string.lower()) or "j" in(string.lower()) or "k" in(string.lower()) or "l" in(string.lower())):
        return("true")
    elif("m" in(string.lower()) or "n" in(string.lower()) or "o" in(string.lower()) or "p" in(string.lower())):
        return("true")
    elif("q" in(string.lower()) or "r" in(string.lower()) or "s" in(string.lower()) or "t" in(string.lower())):
        return("true")
    elif("u" in(string.lower()) or "v" in(string.lower()) or "w" in(string.lower()) or "x" in(string.lower())):
        return("true")
    elif("y" in(string.lower()) or "z" in(string.lower())):
        return("true")
    else:
        return("false")

def Collect_Number(num_in):
    status = "incomplete"
    while (status == "incomplete"):
        if (Alpha_Check(num_in) == "true"):
            num_in = input("Bruh why did you just use letters? Try again:\n\n")
        elif ("." in(num_in)):
            num_in = input("Please enter an integer:\n\n")
        elif ("-" in(num_in)):
            num_in = input("Negative values are not accepted, try again:\n\n")
        elif (" " in(num_in)):
            num_in = input("Please remove spaces: ")
        elif (("." not in(num_in)) and ("-" not in(num_in)) and (" " not in(num_in))):
            status = "complete"
            return(int(num_in))
        else:
            num_in = input("A whoopsie occured. Try again:\n\n")

def Biggest_Multiple_of_2(num_in):
    multiple = 0
    while(num_in/(2**multiple) >= 1):
        multiple += 1
    return(multiple-1)

def Biggest_Multiple_of_10(num_in):
    multiple = 0
    while(num_in/(10**multiple) >= 1):
        multiple += 1
    return(multiple-1)

def Dec_to_Bin(Dec_num):
    Running_Binary_Sum = 0
    while(Dec_num != 0):
        Running_Binary_Sum += 10**(Biggest_Multiple_of_2(Dec_num))
        Dec_num -= 2**(Biggest_Multiple_of_2(Dec_num))
    return(Running_Binary_Sum)

def Bin_to_Dec(Bin_num):
    Running_Decimal_Sum = 0
    while(Bin_num != 0):
        Running_Decimal_Sum += 2**(Biggest_Multiple_of_10(Bin_num))
        Bin_num -= 10**(Biggest_Multiple_of_10(Bin_num))
    return(Running_Decimal_Sum)

print("\n"*20, "This program will take a Binary number and convert it to Decimal,")
print("or take a Decimal number and convert it to Binary", end="\n\n")
print("Please note that only integer values are accepted", end= "\n\n")

Program_State = "running"
while(Program_State == "running"):
    Convert_type = Which_Conversion(input("would you like to convert 1) Binary to Decimal or 2) Decimal to Binary?\n\n"))
    print(end="\n")
    Convert_number = Collect_Number(input("Please enter your number below:\n\n"))
    print(end="\n")
    if(Convert_type == "DtB"):
        print("Your number in binary is: ", Dec_to_Bin(Convert_number), end='\n\n')
    elif(Convert_type == "BtD"):
        print("Your number in decimal is: ", Bin_to_Dec(Convert_number), end='\n\n')
    foo = input("Would you like to convert another number? Yes or No?\n\n")
    foo = foo.lower()
    if("y" in(foo)):
        Program_State = "running"
    elif("n" in(foo)):
        Program_State = "terminated"
    else:
        print("There was an error, so the program assumes you are done")
        Program_State = "terminated"

print("\nThanks for using my program!", end='\n\n')
