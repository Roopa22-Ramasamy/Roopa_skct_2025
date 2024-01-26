# Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city  is the starting location. The number of roads from city  to city  is the first value in the array, from city  to city  is the second, and so on.

# How many paths are there from city  to the last city in the list, modulo ?

# Example


# There are  roads to city ,  roads to city  and  roads to city . The total number of roads is .

# Note
# Pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn.

# Function Description

# Complete the connectingTowns function in the editor below.

# connectingTowns has the following parameters:

# int n: the number of towns
# int routes[n-1]: the number of routes between towns
# Returns

# int: the total number of routes, modulo 1234567.
# Input Format
# The first line contains an integer T, T test-cases follow.

# Each test-case has 2 lines.
# The first line contains an integer N (the number of towns).
# The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1

# Constraints
# 1 <= T<=1000
# 2< N <=100
# 1 <= routes[i] <=1000

# Sample Input

# 2
# 3
# 1 3
# 4
# 2 2 2
# Sample Output

# 3
# 8
# Explanation
# Case 1: 1 route from T1 to T2, 3 routes from T2 to T3, hence only 3 routes.
# Case 2: There are 2 routes from each city to the next, hence 2 * 2 * 2 = 8.


solution :



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
     * Complete the 'connectingTowns' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY routes
     */

    public static int connectingTowns(int n, List<Integer> routes) 
    {
        int result = 1;

        // Calculate the product of all elements in routes and take the modulo
        for (int i = 0; i < n - 1; i++) {
            result = (result * routes.get(i)) % 1234567;

    }
        return result;

}
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> routes = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                    .map(Integer::parseInt)
                    .collect(toList());

                int result = Result.connectingTowns(n, routes);

                bufferedWriter.write(String.valueOf(result));
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

