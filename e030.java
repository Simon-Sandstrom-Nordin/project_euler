import java.util.ArrayList;
import java.util.List;

public class e030 {

    public static void main(String []args) {

        List<Integer> list = new ArrayList<Integer> ();

        for (int k = 1000; k < 1000000; k++) {
            if (check_sum(k)) {
                list.add(k);
            }
        }

        System.out.println("List of numbers:");
        System.out.println(list);
        System.out.println("\n");

        int sum = 0;
        for (int k = 0; k < list.size(); k++) {
            sum += list.get(k);
        }
        System.out.println("Sum of list;");
        System.out.println(sum);

    }

    private static boolean check_sum(int number) {

        // 4 digit number
        if (1000<=number && number<10000) {
            int input_number = number;
            int first = number % 10;
            number -= first;
            int second = number % 100;
            number -= second;
            second = second / 10;
            int third = number % 1000;
            number -= third;
            third = third / 100;
            int fourth = number / 1000;

            double sum = Math.pow(first, 5) + Math.pow(second, 5) + Math.pow(third, 5) + Math.pow(fourth, 5);
            int sum_int = (int) sum;
            // check equality
            if (input_number == sum_int) {
                return true;
            } else {
                return false;
            }
        }

        // 5 digit number
        else if (10000<=number && number<100000) {
            int input_number = number;
            int first = number % 10;
            number -= first;
            int second = number % 100;
            number -= second;
            second = second / 10;
            int third = number % 1000;
            number -= third;
            third = third / 100;
            int fourth = number % 10000;
            number -= fourth;
            fourth = fourth / 1000;
            int fifth = number % 100000;
            fifth = fifth / 10000;

            double sum = Math.pow(first, 5) + Math.pow(second, 5) + Math.pow(third, 5) + Math.pow(fourth, 5) + Math.pow(fifth, 5);
            int sum_int = (int) sum;
            // check equality
            if (input_number == sum_int) {
                return true;
            } else {
                return false;
            }
        }

        // 6 digit number
        else {  //(100000<=number && number<1000000)
            int input_number = number;
            int first = number % 10;
            number -= first;
            int second = number % 100;
            number -= second;
            second = second / 10;
            int third = number % 1000;
            number -= third;
            third = third / 100;
            int fourth = number % 10000;
            number -= fourth;
            fourth = fourth / 1000;
            int fifth = number % 100000;
            number -= fifth;
            fifth = fifth / 10000;
            int sixth = number % 1000000;
            sixth = sixth / 100000;


            double sum = Math.pow(first, 5) + Math.pow(second, 5) + Math.pow(third, 5) + Math.pow(fourth, 5) + Math.pow(fifth, 5) + Math.pow(sixth, 5);
            int sum_int = (int) sum;
            // check equality
            if (input_number == sum_int) {
                return true;
            } else {
                return false;
            }
        }
    }

}

//... this works, but only for four digit numbers...
// Edit: now it works, although the code repetition is insane. Oh well. Interesting there are no
//       digit five powers beyond 194979 ...
