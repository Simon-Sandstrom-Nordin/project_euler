package test;

import java.util.Scanner;

public class islands {

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int symbols = sc.nextInt();

        Integer island_count = countIslands(rows, symbols, sc);
        System.out.println(island_count);

    }

    private static int countIslands(int rows, int symbols, Scanner sc) {
        int count = 0;  // # of completed islands
        for (int r = 1; r <= rows; r++) {
            for (int s = 1; s <= symbols; s++) {
                String symbol = sc.next();


            }
        }

        int count = 3;
        return count;
    }

}

// apparently this "Find # of islands" is a standard question which uses
// graph theory, breadth-first-search / DFS.
// https://www.javatpoint.com/find-number-of-island-in-java
// for algorithm inspiration and shit.
