// Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

// Example



// The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

// Function Description

// Complete the solve function in the editor below.

// solve has the following parameters:

// int n: the number of candy jars
// int operations[m][3]: a 2-dimensional array of operations
// Returns

// int: the floor of the average number of canidies in all jars
// Input Format

// The first line contains two integers,  and , separated by a single space.
//  lines follow. Each of them contains three integers, , , and , separated by spaces.

// Constraints





// Sample Input

// STDIN       Function
// -----       --------
// 5 3         n = 5, operations[] size = 3
// 1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
// 2 5 100
// 3 4 100
// Sample Output

// 160
// Explanation

// Initially each of the jars contains 0 candies

// 0 0 0 0 0  
// First operation:

// 100 100 0 0 0  
// Second operation:

// 100 200 100 100 100  
// Third operation:

// 100 200 200 200 100  
// Total = 800, Average = 800/5 = 160


solution:

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY operations
     */

    public static int solve(int n, List<List<Integer>> operations) {
    // Write your code here

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> operations = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                operations.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.solve(n, operations);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

