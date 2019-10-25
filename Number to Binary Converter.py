#!/home/derickson/Projects/SpongeBob/Number\ to\ Binary\ Converter.py
print("\n"*20, "This program will take a Binary number and convert it to Decimal,")
print("or take a Decimal number and convert it to Binary", end="\n\n")
print("Please note that only integer values are accepted", end= "\n\n")

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
        else:
            conv_type_in = input("A whoopsie occured. Try again.\n\n")
            status = "incomplete"
    print(end= '\n\n')

def Collect_Number(num_in):
    status = "incomplete"
    while (status == "incomplete"):
        if (("." not in(num_in)) and ("-" not in(num_in)) and (" " not in(num_in))):
            status = "complete"
            return(int(num_in))
        elif ("." in(num_in)):
            num_in = input("Please enter an integer:\n\n")
        elif ("-" in(num_in)):
            num_in = input("Negative values are not accepted, try again:\n\n")
        elif (" " in(num_in)):
            num_in = input("Please remove spaces:")
        else:
            num_in = input("A whoopsie occured. Try again.\n\n")

Convert_type = Which_Conversion(input("would you like to convert 1) Binary to Decimal or 2) Decimal to Binary?\n\n"))
print(Convert_type, "\n", type(Convert_type))
Convert_number = Collect_Number(input("Please enter your number below:\n\n"))
print(Convert_number, "\n", type(Convert_number))

############################################
#def Bin_to_Dec(Bin_num):
############################################

def Dec_to_Bin(Dec_num):
    Running_Binary_Sum = 0
    active = "true"
    while (Dec_num > 0, active == "true"):
        if (Dec_num > 255):
            print("Error: number too large, I haven't programmed outside of 8 Bits yet\n")
            active = "false"
        elif (Dec_num >= 128):
            Running_Binary_Sum += 10000000
            Dec_num -= 128
        elif (Dec_num >= 64):
            Running_Binary_Sum += 1000000
            Dec_num -= 64
        elif (Dec_num >= 32):
            Running_Binary_Sum += 100000
            Dec_num -= 32
        elif (Dec_num >= 16):
            Running_Binary_Sum += 10000
            Dec_num -= 16
        elif (Dec_num >= 8):
            Running_Binary_Sum += 1000
            Dec_num -= 8
        elif (Dec_num >= 4):
            Running_Binary_Sum += 100
            Dec_num -= 4
        elif (Dec_num >= 2):
            Running_Binary_Sum += 10
            Dec_num -= 2
        elif (Dec_num >= 1):
            Running_Binary_Sum += 1
            Dec_num -= 1
            active = "false"
    return(Running_Binary_Sum)

print("Convert number=", Convert_number)
Dec_to_Bin(Convert_number)
print("Thanks for using my program!")
