package test.java_tasks;
import java.util.Scanner;

public class ProblemA {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // Number of strings
        Integer number = sc.nextInt();

        // String to hold concatenated words
        String concat = "";

        for (int word = 0; word <= number; word ++) {
            concat += sc.nextLine().strip();
        }

        System.out.println(concat);

    }

}
