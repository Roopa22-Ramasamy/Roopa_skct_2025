1)	Question 
Task
Given an integer, , perform the following conditional actions:
•	If  is odd, print Weird
•	If  is even and in the inclusive range of  to , print Not Weird
•	If  is even and in the inclusive range of  to , print Weird
•	If  is even and greater than , print Not Weird
Input Format
A single line containing a positive integer, .
Constraints
•	
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
Sample Input 0
3
Sample Output 0
Weird
Explanation 0

 is odd and odd numbers are weird, so print Weird.
Sample Input 1
24
Sample Output 1
Not Weird

solution :

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")


2) question

Task
The provided code stub reads two integers,  and , from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
No rounding or formatting is necessary.
Example


•	The result of the integer division .
•	The result of the float division is .
Print:
0
0.6
Input Format
The first line contains the first integer, .
The second line contains the second integer, .
Output Format
Print the two lines as described above.
Sample Input 0
4
3
Sample Output 0
1
1.33333333333

solution :

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
