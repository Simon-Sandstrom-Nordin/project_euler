public class e012 {

    public static void main(String []args) {

        int base = 1;
        int current_number = 0;
        int record = 0;
        boolean searching = true;
        while (searching) {
            current_number += base;
            if (numberOfDivisors(current_number) > record) {
                record = numberOfDivisors(current_number);
                System.out.println(record);
            }
            if (numberOfDivisors(current_number) > 500) {
                searching = false;
            }
            base += 1;
        }
        System.out.println(current_number);

    }

    private static int numberOfDivisors(int integer) {
        int counter = 0;

        for (int i = 1; i <= integer ; i++) {
            if (integer % i == 0) {
                counter += 1;
            }

        }

        return counter;
    }

}
