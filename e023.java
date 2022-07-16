// Non-abundant sums
// def: Perfect number. Sum of proper divisors is equal
//     to the number
// def: Deficient number. -II- is less than number.
// def: Abundant number. -II- ins greater than number.

import java.util.ArrayList;
import java.util.List;

public class e023 {

    public static void main(String []args) {

        List<Integer> abundant = new ArrayList<Integer>();
        int divisors = 0;
        int number_type = 0;
        for (int i = 1; i <= 28123; i++) {
            divisors = proper_divisors(i);
            number_type = type_of_number(i, divisors);
            if (number_type == 1) {
                abundant.add(i);
            }
        }

        int sum_proper_divisors = 0;
        for (int h = 1; h <= 28123; h++) {
                boolean sum_of_two_abundant_numbers = false;
                for (int i = 0; i < abundant.size(); i++) {
                    for (int k = 0; k < abundant.size(); k++) {
                        if (h == abundant.get(i) + abundant.get(k)) {
                            sum_of_two_abundant_numbers = true;
                        }
                    }
                }
            if (sum_of_two_abundant_numbers == false) {
                sum_proper_divisors += h;
            }
            if (h % 100 == 0) {
                System.out.println(h);
            }
        }

        System.out.println(sum_proper_divisors);    // answer: 4179871
    }

    private static int proper_divisors(int number) {
        int sum = 0;
        for (int i = 1; i < number; i++) {
            if (number % i == 0) {
                sum += i;
            }
        }
        return sum;
    }

    private static int type_of_number(int number, int divisors) {
        int number_type = 0;
        if (number < divisors) {
            number_type += 1;
        }   // abundant
        else if (number > divisors) {
            number_type -= 1;
        }   // deficient
        return number_type;
    }

}
