public class e036 {

    public static void main(String[] args) {

        int sum_prime = 0;
        for (int k = 1; k < 1000000; k ++) {
            if (palindrome_checker(k) && binary_checker(k)) {
                sum_prime += k;
            }
        }
        System.out.println(sum_prime);

    }

    private static boolean palindrome_checker(int number) {
        String number_string = Integer.toString(number);
        String reverse_string = "";
        for (int k = number_string.length() - 1; k >= 0 ; k--) {
            reverse_string += number_string.charAt(k);
        }
        return number_string.equals(reverse_string);
    }

    private static boolean binary_checker(int number) {
        String binary_string = "";
        while (number > 1) {
            binary_string += Integer.toString(number % 2);
            number -= number % 2;
            number = number / 2;
        }
        binary_string += Integer.toString(number);

        String reverse_string = new StringBuilder(binary_string).reverse().toString();
        return binary_string.equals(reverse_string);
    }

}
