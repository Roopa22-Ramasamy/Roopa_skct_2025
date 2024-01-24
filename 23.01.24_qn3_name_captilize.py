# 1) You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Function Description

# Complete the print_full_name function in the editor below.

# print_full_name has the following parameters:

# string first: the first name
# string last: the last name
# Prints

# string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
# Input Format

# The first line contains the first name, and the second line contains the last name.

# Constraints

# The length of the first and last names are each ≤ .

# Sample Input 0

# Ross
# Taylor
# Sample Output 0

# Hello Ross Taylor! You just delved into python.
# Explanation 0

# The input read by the program is stored as a string data type. A string is a collection of characters.

# answer:


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

-------------------------------------------------------------------------------------------------------------------------

# 2)You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


# Given a full name, your task is to capitalize the name appropriately.

# Input Format

# A single line of input containing the full name, .

# Constraints

# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Output Format

# Print the capitalized string, .

# Sample Input

# chris alan
# Sample Output

# Chris Alan


solution:

def solve(s):
    a = s.split(' ')
    a1 = (((i.capitalize() for i in a)))
    return ' '.join(a1)
