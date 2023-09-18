import java.util.Comparator;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class kth_javap_bonus {
    public static void main(String[] args) {
        int[] numbers = readNumbers();
        Scanner sc = new Scanner(System.in);
        checkResults(numbers, sc);
    }

    private static int[] readNumbers() {
        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[2];
        numbers[0] = sc.nextInt(); // N: antal betyg
        int date_int = sc.nextInt();
        String date = String.valueOf(date_int);
        int year = Integer.parseInt(date.substring(0, 4));
        int month = Integer.parseInt(date.substring(4, 6));
        int day = Integer.parseInt(date.substring(6, 8));
        int day_count = 365 * year + 31 * month + day;
        numbers[1] = day_count;
        return numbers;
    }

    private static void checkResults(int[] numbers, Scanner sc) {
        TreeMap<String, Integer> student_scores = new TreeMap<>(new Comparator<String>() {
            @Override
            public int compare(String fullName1, String fullName2) {
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

        for (int i = 1; i <= numbers[0]; i++) {
            String student = sc.nextLine();
            String extractDate = student.substring(0, 8);
            int year = Integer.parseInt(extractDate.substring(0, 4));
            int month = Integer.parseInt(extractDate.substring(4, 6));
            int day = Integer.parseInt(extractDate.substring(6, 8));
            int day_count = 365 * year + 31 * month + day;
            student = student.substring(9, student.length());
            String[] namesAndScores = student.split(" ");
            String firstName = namesAndScores[0];
            String lastName = namesAndScores[1];
            String fullName = firstName + " " + lastName;
            int score = Integer.parseInt(namesAndScores[2]);

            if (day_count <= numbers[1]) {
                try {
                    int current_score = student_scores.get(fullName);
                    if (score > current_score) {
                        student_scores.put(fullName, score);
                    }
                } catch (NullPointerException e) {
                    student_scores.put(fullName, score);
                }
            }
        }

        if (student_scores.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Map.Entry<String, Integer> entry : student_scores.entrySet()) {
                String fullName = entry.getKey();
                int score = entry.getValue();
                System.out.println(fullName + " " + score);
            }
        }
    }
}
