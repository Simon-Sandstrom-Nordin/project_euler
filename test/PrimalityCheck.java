package test;
import java.util.Scanner;

public class PrimalityCheck {

    public static void main(String []args) {
        long sum = sumUpNumber();
        // System.out.println("---");
        // System.out.println(sum);
        // System.out.println("---");
        long prime = findLowestPrimeFactor(sum);
        System.out.println(prime);
    }

    private static long sumUpNumber() {
        long sum = 0;    // for now
        Scanner sc = new Scanner(System.in);
        long numberOfNumbers = sc.nextLong();
        for (int k = 1; k <= numberOfNumbers; k++) {
            long term = sc.nextLong();
            sum = sum + term;
        }
        return sum;
    }

    private static long findLowestPrimeFactor(long number) {
        long prime = 0;  // for now
        for (long k = 2; k <= number; k++) {
            if (number % k == 0) {
                prime = k;
                break;
            }
        }
        return prime;
    }

}

// ... leave this for now.

// back 26/9 - 22.
// edit: changed all Integer data types to long.
// I think some test cases use numbers up to 10^12.
// That worked, we got all 5/5 test cases now.
