import java.util.Scanner;

public class e002 {

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        int fibonacci_counter = fibonacci();
        System.out.println(fibonacci_counter);

    }

    public static int fibonacci() {
        int first_number = 1;
        int second_number = 2;
        int temporary_number = 0;
        int counter = second_number;
        while (second_number <= 4000000) {
            temporary_number = second_number;
            second_number += first_number;
            first_number = temporary_number;
            if (second_number % 2 == 0) {
                counter += second_number;
            }

        }

        return counter;

    }

}
