import java.util.*;

public class kth_javap_bonus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt(); // N: antal betyg
        int date = sc.nextInt(); // D: specified date
        sc.nextLine(); // Consume the remaining newline character

        Map<String, Result> resultMap = new HashMap<>();

        for (int i = 0; i < count; i++) {
            String line = sc.nextLine();
            String[] parts = line.split(" ");

            int resultDate = Integer.parseInt(parts[0]);
            if (resultDate <= date) {
                String firstName = parts[1];
                String lastName = parts[2];
                int score = Integer.parseInt(parts[3]);

                String fullName = firstName + " " + lastName;

                if (!resultMap.containsKey(fullName) || resultMap.get(fullName).score < score) {
                    resultMap.put(fullName, new Result(resultDate, firstName, lastName, score));
                }
            }
        }

        List<Result> results = new ArrayList<>();
        for (Result result : resultMap.values()) {
            results.add(result);
        }

        if (results.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            Collections.sort(results);
            for (Result result : results) { // enhanced for loop, for-each-loop
                System.out.println(result.toString());
            }
        }
    }

    public static class Result implements Comparable<Result> {
        int resultDate;
        String firstName;
        String lastName;
        int score;

        public Result(int resultDate, String firstName, String lastName, int score) {
            this.resultDate = resultDate;
            this.firstName = firstName;
            this.lastName = lastName;
            this.score = score;
        }

        @Override
        public int compareTo(Result other) {
            int lastNameComparison = this.lastName.compareTo(other.lastName);
            if (lastNameComparison != 0) {
                return lastNameComparison;
            } else {
                return this.firstName.compareTo(other.firstName);
            }
        }

        @Override
        public String toString() {
            return resultDate + " " + firstName + " " + lastName + " " + score;
        }
    }
}
