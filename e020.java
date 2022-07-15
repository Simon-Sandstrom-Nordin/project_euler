// Lesson learnt from developing this program:
// Data type int stores whole numbers ± 2,147,483,647
// Data type float stores whole numbers ± 9,223,372,036,854,775,807
// 100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
// Thus it is sad in Java...
// ... I think there's a Big Int package? Mhm?

public class e020 {

    public static void main(String []args) {
        int number = 25;
        long fact = factorial(number);
        String fact_string = Long.toString(fact);
        int sum = 0;
        System.out.println(fact);
        for (int i = 0; i < fact_string.length(); i ++) {
            sum += Integer.parseInt(String.valueOf(fact_string.charAt(i)));
        }

        System.out.println(sum);

        // So that was useless. Instead, let's use python to find the value of 100!:
        String value = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000";
        long cheat_sum = 0;
        for (int i = 0; i < value.length(); i ++) {
            cheat_sum += Integer.parseInt(String.valueOf(value.charAt(i)));
        }

        System.out.println(cheat_sum);
    }

    private static long factorial(int number) {
        if (number == 0 || number == 1) {
            return 1;
        }
        return number * factorial(number-1);
    }

}
