package test.java_tasks;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class ProblemF {

    public static void main(String []args) {

            int[] numbers = readNumbers();
            checkResults(numbers);

    }

    private static int[] readNumbers() {

    Scanner sc = new Scanner(System.in);

    int[] numbers = new int[2];
    numbers[0] = sc.nextInt();  // N: antal betyg
    // vi kommer omvandla datumet till antal dagar efter 00000101
    int date_int = sc.nextInt();
    String date = String.valueOf(date_int);
    int year = Integer.parseInt(date.substring(0,4));
    int month = Integer.parseInt(date.substring(4,6));
    int day = Integer.parseInt(date.substring(6,8));
    //System.out.println(year);
    //System.out.println(month);
    //System.out.println(day);
    // This conversion will ignore leap years - might be good enough for kattis
    // nvm leap years don't matter the point is to order them chronologically
    // also varying month lengths but again -_(^.^)_-
    int day_count = 365 * year + 31* month + day;
    numbers[1] = day_count;
    return numbers;
    }

    private static void checkResults(int[] numbers) {

        Scanner sc = new Scanner(System.in);
        Map<String, Integer> student_scores = new HashMap<>();
        Map<String, Integer> student_dates = new HashMap<>();

        // read in students and enter them into the HashMap with student_scores
        // if appropriate
        for (int i = 1; i <= numbers[0]; i++) {
            String student = sc.nextLine();
            // extract date
            String extractDate = student.substring(0,8);
            // calculate day count
            int year = Integer.parseInt(extractDate.substring(0,4));
            int month = Integer.parseInt(extractDate.substring(4,6));
            int day = Integer.parseInt(extractDate.substring(6,8));
            int day_count = 365 * year + 31* month + day;
            // remove date from student string
            student = student.substring(9, student.length());   // 9 cuz whitespace
            //System.out.println(student);
            //System.out.println(day_count);
            //counts.put(subseq, counts.getOrDefault(subseq, 0) + 1);
            String[] namesAndScores = student.split(" ");
            String firstName = namesAndScores[0];
            String lastName = namesAndScores[1];
            String fullName = firstName + " " + lastName;
            int score = Integer.parseInt(namesAndScores[2]);
            //System.out.println(firstName);
            //System.out.println(lastName);
            //System.out.println(score);
            //System.out.println(fullName);

            if (day_count <= numbers[1]) {
                try {
                int current_score = student_scores.get(fullName);
                if (score > current_score) {
                student_scores.put(fullName, score);
                student_dates.put(fullName, Integer.parseInt(extractDate));
                }

                } catch (NullPointerException e) {   // means they're not in the map yet
                student_scores.put(fullName, score);
                student_dates.put(fullName, Integer.parseInt(extractDate));
                }
            }

        }

/*         for (Map.Entry<String, Integer> entry : student_scores.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("Key: " + key + ", Value: " + value);
        }
        for (Map.Entry<String, Integer> entry : student_dates.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("Key: " + key + ", Value: " + value);
        } */

    }

}
