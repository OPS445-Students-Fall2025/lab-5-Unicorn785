#!/usr/bin/env python3
# Author ID: Pirajeen Kandasamy

# If the input cannot be converted to numbers, it returns an error message.
def add(number1, number2):
    try:
        # Convert both inputs to integers
        num1 = int(number1)
        num2 = int(number2)
        # Add them together
        result = num1 + num2
        return result
    except:
        # if it gets mixed with numbers and alphabets it returns a error
        return 'error: could not add numbers'


#open and read a file and it will return a list of lines from the file (each ending with '\n').
#if the file doesnt  exist or can`t be opened, it returns an error message.
def read_file(filename):
    try:
        # Open the file in read mode
        f = open(filename, 'r')
        # Read all lines from the file into a list
        lines = f.readlines()
        # Close the file
        f.close()
        # Return the list of lines
        return lines
    except:
        # If something goes wrong (like the file not being found)
        return 'error: could not read file'


# main block
if __name__ == '__main__':
    # Test add() with different kinds of input
    print(add(10, 5))                # should print 15
    print(add('10', 5))              # should print 15
    print(add('abc', 5))             # should print error message

    # Test read_file() with valid and invalid file names
    print(read_file('seneca2.txt'))  # should show file contents
    print(read_file('file10000.txt'))# should print error message
