import java.util.*;

public class e032 {

    public static void main(String []args) {

        List<Integer> products = new ArrayList<>();
        //check_pandigital(45, 46);
        double sum = 0;
        Set<Double> product_set = new HashSet<Double>();

        for (long multiplicand = 1; multiplicand < 999999; multiplicand ++) {
            for (long multiplier = 1; multiplier < 999999; multiplier ++) {
                double product = check_pandigital(multiplicand, multiplier);
                if (product_set.contains(product) == false) {
                    sum += product;
                    product_set.add(product);
                }
            }
        }
        System.out.println(sum);
    }

    private static long check_pandigital(long multiplicand, long multiplier) {

        long product = multiplicand * multiplier;
        String number_string = Long.toString(product) + Long.toString(multiplicand) + Long.toString(multiplier);
        Set<String> all_numbers = new HashSet<String>();
        for (int i=0;i<number_string.length();i++) {
            if (all_numbers.contains(number_string.substring(i, i+1))) {
                return 0;   // if it already contains the thing, then it shouldn't qualify.
            }
            all_numbers.add(number_string.substring(i, i+1));
        }
        all_numbers.remove("0");
        if (all_numbers.size() == 9) {  // zero not included
            return product;
        } else return 0;
    }

}
