public class Main {

    public static void main(String args[]) {
        int x = 5;
        int res = factorial(x);
        System.out.println(res); 
    }

    private static int factorial(int x) {
        if (x == 1) {
            return 1;
        } 
        return x * factorial(x-1);
    }

}
