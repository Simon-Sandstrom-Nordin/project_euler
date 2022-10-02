package test;
import java.util.Scanner;

public class main {

    public static void main(String []args) {

        Scanner sc = new Scanner(System.in);
        Integer numberOfWords = sc.nextInt();
        String wordHolder = "";
        for (int i = 1; i <= numberOfWords; i++) {
            String word = sc.next();
            wordHolder = wordHolder + word;
        }   // note string concatenation in loop
        System.out.println(wordHolder);

    }

}
