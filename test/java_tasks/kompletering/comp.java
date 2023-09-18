import java.lang.Comparable;
import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
import java.util.TreeMap;
// import java.util.Arrays;


public class kth_javap_bonus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = readNumbers(sc);
        checkResults(numbers, sc);
    }


    public static class Result implements Comparable<String> {

    String firstName;
    String lastName;
    String fullName;
    int score;
    String extractDate;

    Map<String, String> student_dates = new HashMap<>();
    TreeMap<String, Integer> student_scores = new TreeMap<>(new Comparable<String>() {
    @Override
    public int compareTo(String fullName1, String fullName2) {
        String[] name1Parts = fullName1.split(" ");
        String lastName1 = name1Parts[name1Parts.length - 1];
        String[] name2Parts = fullName2.split(" ");
        String lastName2 = name2Parts[name2Parts.length - 1];
        int lastNameComparison = lastName1.compareTo(lastName2);
        if (lastNameComparison != 0) {
            return lastNameComparison;
        } else {
            String firstName1 = name1Parts[0];
            String firstName2 = name2Parts[0];
            return firstName1.compareTo(firstName2);
        }
    }
    });
    }

    private static int[] readNumbers(Scanner sc) {
        int[] numbers = new int[2];
        numbers[0] = sc.nextInt(); // N: antal betyg

        // räkna dagar sedan och till och med 00000101
        int date = sc.nextInt(); // D: specified date
        String dateString = String.valueOf(date);
        int year = Integer.parseInt(dateString.substring(0, 4));
        int month = Integer.parseInt(dateString.substring(4, 6));
        int day = Integer.parseInt(dateString.substring(6, 8));
        int dayCount = 365 * year + 31 * month + day;
        numbers[1] = dayCount;
        return numbers;
    }

    private static void checkResults(int[] numbers, Scanner sc) {
        sc.nextLine(); // Consume the remaining newline character
        kth_javap_bonus.Result result_map = new kth_javap_bonus.Result();

        for (int i = 0; i < numbers[0]; i++) {
            kth_javap_bonus.Result student_instance = new kth_javap_bonus.Result();
            String student = sc.nextLine();
            int year = Integer.parseInt(student.substring(0, 4));
            int month = Integer.parseInt(student.substring(4, 6));
            int day = Integer.parseInt(student.substring(6, 8));
            int day_count = 365 * year + 31 * month + day;
            student = student.substring(9); // Remove the date part
            String[] namesAndScores = student.split(" ");
            student_instance.firstName = namesAndScores[0];
            student_instance.lastName = namesAndScores[1];
            student_instance.fullName = namesAndScores[0] + " " + namesAndScores[1];
            student_instance.score = Integer.parseInt(namesAndScores[2]);
            student_instance.extractDate = student.substring(0, 8);

            if (day_count <= numbers[1]) {
                if (!result_map.get(student_scores).containsKey(student_instance.get(fullName)) || student_instance.get(score) > result_map.get(student_scores).get(student_instance.get(fullName))) {
                    result_map.get(student_scores).put(student_instance.get(fullName), student_instance.get(score));
                    result_map.get(student_dates).put(student_instance.get(fullName), student_instance.get(extractDate));
                }
            }
        }

        if (result_map.student_scores.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Map.Entry<String, Integer> entry : result_map.get(student_scores).entrySet()) {
                String fullName = entry.getKey();
                String dateExtract = result_map.get(student_dates).get(fullName);
                int score = entry.getValue();
                System.out.println(dateExtract + " " + fullName + " " + score);
            }
        }
    }
}
