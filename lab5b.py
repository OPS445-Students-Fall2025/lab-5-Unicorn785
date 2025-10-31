#!/usr/bin/env python3
# Author ID: pirajeen kandasamy

#lab5a.py
def read_file_string(file_name):
#Return entire file contents as one string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
#Return file contents as a list of lines without trailing newlines.
    with open(file_name, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]

#lab5b.py
def append_file_string(file_name, string_of_lines):
# Takes two strings file name and string of lines. creates file if missing, if not formed together.
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
#Takes a string (file_name) and a list (list_of_lines).
#Writes each item as one line to the file (overwrites/creates file).

    with open(file_name, 'w') as f:
        for item in list_of_lines:
            f.write(str(item) + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
        # Step 1: Read all lines from the source file and remove newline characters
    lines = read_file_list(file_name_read)

    # Step 2: Open the destination file for writing (this will overwrite existing content)
    with open(file_name_write, 'w') as new_file:

        # Step 3: Go through each line from the original file
        line_number = 1  # Start counting from 1

        for line in lines:
            # Write the line number, a colon, and then the line text
            new_file.write(str(line_number) + ':' + line + '\n')

            # Increase the line number for the next line
            line_number = line_number + 1

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
