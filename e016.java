// doesn't work... maybe 2^1000 is too big?

public class e016 {

    public static void main(String []args) {

        double number = Math.pow(2, 1000);
        double sum = sumFunction(number);
        System.out.println(sum);

    }

    private static double sumFunction(double number) {
        double sum = 0;

        while (number > 0) {
            double digit = number % 10;
            number = Math.floor(number / 10);
            sum += digit;
        }

        return sum;

    }

}
