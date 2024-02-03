# Given a number N reverse the number and print it.

# Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

# Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

# Input Format

# 123

# Constraints

# N <= 1000

# Output Format

# 321

# Sample Input 0

# 123
# Sample Output 0

# 321
# Sample Input 1

# 2341
# Sample Output 1

# 1432


solution:

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) 
    {
       Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int rev = 0;
        while(n>0)
        {
            int rem = n%10;   //last digit
            rev = rev*10+rem;
            n = n/10;    //removes last digit
        }
        System.out.print(rev);
    }
}

--------------------------------------------------------------------------------------------------------------------------

2)
# Given an integer N, write a program to count the number of digits in N.

# Input Format

# Example 1: Input0: N = 12345

# Example 2: Input1: N = 8394

# Constraints

# n <= 10000

# Output Format

# Output0: 5 Explanation: N has 5 digits

# Output1: 4 Explanation: N has 4 digits

# Sample Input 0

# 12345
# Sample Output 0

# 5
# Sample Input 1

# 876349
# Sample Output 1

# 6


solution:

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        while(n>0)
        {
             n = n/10;   //removes last digit
            count++;
        }
        System.out.print(count);
    }
}


