package garbage;
import java.util.Scanner;   // imports Scanner class

public class test_exception {

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter favorite film");
        Integer film = null;

        // So this is how try-except(catch?) things work in Java...
        try {
            film = Integer.valueOf(sc.nextLine());
        } catch (Exception e) { // blanc space / alphabet input gave
                                // java.lang.NumberFormatException
                                // ... meaning that the input could not be
                                // parsed into an integer.
            System.out.println(e);
        }

        System.out.println(film);

    }

}
// you know, exploring Java isn't so bad...
