// Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

// Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

// Input Format

// A single integer denoting .

// Constraints

// Output Format

// Print an integer denoting the best divisor of .

// Sample Input 0

// 12
// Sample Output 0

// 6
// Explanation 0

// The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.


solution:


import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        int result = bestDivisor(n);

        System.out.println(result);

        bufferedReader.close();
    }

   
    public static int digitSum(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }

    
    public static int bestDivisor(int n) {
        int bestDivisor = 1;
        int maxDigitSum = 1;

        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                int currentDigitSum = digitSum(i);
                if (currentDigitSum > maxDigitSum || (currentDigitSum == maxDigitSum && i < bestDivisor)) {
                    maxDigitSum = currentDigitSum;
                    bestDivisor = i;
                }
            }
        }

        return bestDivisor;
    }
}
