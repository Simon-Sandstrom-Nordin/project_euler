package test.java_tasks;
import java.util.Scanner;

public class ProblemB {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // Number of terms
        long terms = sc.nextLong();

        // Sum up terms
        long sum = 0;
        for (long term = 1; term <= terms; term ++) {
            sum += sc.nextLong();
        }

        // Find the least prime factor
        long prime = 0;
        for (long k = 2; k <= sum; k ++) {
            if (sum % k == 0) {
                prime = k;
                break;
            }
        }

        System.out.println(prime);

    }

}
