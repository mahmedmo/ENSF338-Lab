import sys
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes') 
# Test the function
do_stuff()

# (i)   The code takes in a number that is inputted as the file is run and changes it into an int. 
#       It prints no if the number is less than 2 or if the number is divisible by a number other than 1 and itself (if the number is composite).
#       It prints yes if the number is not divisible by any numbers besides 1 and itself, meaning the number is prime.
#       So the code prints yes if the number is a prime number.

# (ii)  An error in the code is that the second quotation mark in line 11 is not standard, 
#       so it isn't recognized as the closing quotation mark in the print statement.