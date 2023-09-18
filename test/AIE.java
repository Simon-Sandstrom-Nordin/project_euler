package test.java_tasks;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class IslandCounter {
    private int rows;
    private int cols;
    private boolean[][] visited;

    public IslandCounter(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        visited = new boolean[rows][cols];
    }

    public int countIslands(char[][] seaMap) {
        int count = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (seaMap[i][j] == '@' && !visited[i][j]) {
                    count++;
                    exploreIsland(seaMap, i, j);
                }
            }
        }

        return count;
    }

    private void exploreIsland(char[][] seaMap, int startRow, int startCol) {
        Queue<int[]> queue = new LinkedList<>();
        // lägger in en tvåelementig 1D-array med integers
        queue.offer(new int[]{startRow, startCol});

        while (!queue.isEmpty()) {
        // tar fram var vi är
            int[] position = queue.poll();
            int row = position[0];
            int col = position[1];

            // kollar vår position och försöker kolla de närliggande rekursivt
            if (isValidPosition(row, col) && seaMap[row][col] == '@' && !visited[row][col]) {
                visited[row][col] = true;
                queue.offer(new int[]{row - 1, col}); // Up
                queue.offer(new int[]{row + 1, col}); // Down
                queue.offer(new int[]{row, col - 1}); // Left
                queue.offer(new int[]{row, col + 1}); // Right
            }
        }
    }

    private boolean isValidPosition(int row, int col) {
        return row >= 0 && row < rows && col >= 0 && col < cols;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Number of characters per column
        int rows = scanner.nextInt();
        // Number of characters per row
        int cols = scanner.nextInt();

        char[][] seaMap = new char[rows][cols];

        // Enter sea map row by row
        for (int i = 0; i < rows; i++) {
            seaMap[i] = scanner.next().toCharArray();
        }

        IslandCounter islandCounter = new IslandCounter(rows, cols);
        int result = islandCounter.countIslands(seaMap);
        // Print the number of islands
        System.out.println(result);
    }
}
