package test.test.java_tasks;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class UniqueSubsequence {
    public static int findUniqueSubsequence(int N, String sequence) {
        if (N > sequence.length()) {
            return -1;
        }

        Map<String, Integer> counts = new HashMap<>();

        // Räkna antalet förekomster av delsekvenser av längd N
        for (int i = 0; i <= sequence.length() - N; i++) {
            String subseq = sequence.substring(i, i + N);
            counts.put(subseq, counts.getOrDefault(subseq, 0) + 1);
        }

        // Hitta den första unika delsekvensen
        for (int i = 0; i <= sequence.length() - N; i++) {
            String subseq = sequence.substring(i, i + N);
            if (counts.get(subseq) == 1) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        String sequence = scanner.next();

        int start_position = findUniqueSubsequence(N, sequence);
        System.out.println(start_position);
    }
}
