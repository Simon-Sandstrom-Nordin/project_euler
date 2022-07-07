// Collatz problem

public class e014 {

    public static void main(String []args) {
        int record = 0;
        for (int i = 1; i < 1000000; i++) {
            if (i % 100 == 0) {
                System.out.println(i);
            }
            int score = counter(i);
            if (score > record) {
                record = score;
            }
        }

        System.out.println(record);

    }

    private static int counter(int number) {
        int counter = 1;    // base case is 1
        boolean searching = true;
        while (searching) {
            counter += 1;
            number = collatz(number);
            if (number == 1) {
                searching = false;
            }
        }
        return counter;

    }

    private static int collatz(int number) {
        if (number % 2 == 0) {
            return number / 2;
        } else {
            return 3*number + 1;
        }

    }

}
