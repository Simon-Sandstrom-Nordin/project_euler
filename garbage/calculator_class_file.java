package garbage;
import java.util.Scanner;

public class calculator_class_file {

    public static void main(String []args) {

        System.out.println("Calculator!");
        int c = add();
        System.out.println("The result is " + c + ".");




    }

    private static int add() {
        Scanner sc = new Scanner(System.in);    //Scanner object

        System.out.println("Enter first number:");
        int a = sc.nextInt();

        System.out.println("Enter second number:");
        int b = sc.nextInt();
        return a + b;

    }

}
