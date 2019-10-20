#!/home/derickson/Projects/SpongeBob/Number\ to\ Binary\ Converter.py

print("\n"*20, "This program will take a Binary number and convert it to Decimal,")
print("or take a Decimal number and convert it to Binary", end="\n\n")
print("Please note that only integer values are accepted", end= "\n\n")
Convert_type = input("Would you like to convert 1) Binary to Decimal or 2) Decimal to Binary?\n\n")
#if ("1" in(Convert_type)):
#    Convert_type = "BtD"
#elif ("binary to decimal" in(Convert_type.lower):
#    Convert_type = "BtD"
#elif ("2" in(Convert_type)):
#    Convert_type = "DtB"
#elif ("decimal to binary" in(Convert_type.lower):
#    Convert_type = "DtB"
#else:
#    print("Bruh try again")
#    exit()

Convert_type = ("BtD" if ("1" in(Convert_type)) else "DtB")

#Create global variables to avoid errors
Convert_number = 0
Digit_1="0"
Digit_2="0"
Digit_3="0"
Digit_4="0"
Digit_5="0"
Digit_6="0"
Digit_7="0"
Digit_8="0"
def Collect_Number():
    global Convert_number
    Convert_number = input("\nPlease enter your number below:\n")
    if ("." in(str(Convert_number))):
        print("\nStop, you have violated the law!")
        Convert_number = input("Enter an integer like the directions clearly stated\n")
Collect_Number()






############################################
############################################
#def Bin_to_Dec(Bin_num):

def Dec_to_Bin(Dec_num):
    #Make Dec_num an integer
    Dec_num = int(Dec_num)

    #Reset the global variables
    global Digit_1
    Digit_1 = "0"
    global Digit_2
    Digit_2 = "0"
    global Digit_3
    Digit_3 = "0"
    global Digit_4
    Digit_4 = "0"
    global Digit_5
    Digit_5 = "0"
    global Digit_6
    Digit_6 = "0"
    global Digit_7
    Digit_7 = "0"
    global Digit_8
    Digit_8 = "0"

    #Calculate the Binary number
    while (Dec_num > 0):
        if (Dec_num > 255):
            print("Error: number too large, I haven't programmed outside of 8 Bits yet\n")
        elif (Dec_num >= 128):
            Digit_8 = "1"
            Dec_num -= 128
        elif (Dec_num >= 64):
            Digit_7 = "1"
            Dec_num -= 64
        elif (Dec_num >= 32):
            Digit_6 = "1"
            Dec_num -= 32
        elif (Dec_num >= 16):
            Digit_5 = "1"
            Dec_num -= 16
        elif (Dec_num >= 8):
            Digit_4 = "1"
            Dec_num -= 8
        elif (Dec_num >= 4):
            Digit_3 = "1"
            Dec_num -= 4
        elif (Dec_num >= 2):
            Digit_2 = "1"
            Dec_num -= 2
        elif (Dec_num >= 1):
            Digit_1 = "1"
            Dec_num -= 1
        else:
            break
######################################
######################################

#if (Convert_type == "DtB" and {[(insert a limit here)]}:
Dec_to_Bin(Convert_number)
print(Digit_8,Digit_7,Digit_6,Digit_5, " ", Digit_4,Digit_3,Digit_2,Digit_1,sep='',end='\n\n')
#else:
    #print("A Whoopsie occured!")

print("Thanks for using my program!")
