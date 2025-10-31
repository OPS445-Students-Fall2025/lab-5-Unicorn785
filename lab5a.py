#!/usr/bin/env python3
#Author ID:pkandasamy7

def read_file_string(file_name):
#Takes file_name (str) and returns the entire file contents as a string.
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
#Takes file_name (str) and returns the file contents as a list of lines with newline characters removed.
    
    with open(file_name, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
