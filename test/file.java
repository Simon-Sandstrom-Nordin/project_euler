import java.util.Scanner;

public class file {
    private static int rows;
    private static int cols;
    private static char[][] seaMap;
    private static boolean[][] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Number of characters per column
        rows = scanner.nextInt();
        // Number of characters per row
        cols = scanner.nextInt();
        scanner.nextLine();

        seaMap = new char[rows][cols];
        visited = new boolean[rows][cols];

        // Enter sea map row by row
        for (int i = 0; i < rows; i++) {
            String row = scanner.nextLine();
            seaMap[i] = row.toCharArray();
        }

        int count = 0;

        // Process sea map and count islands
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (seaMap[i][j] == '@' && !visited[i][j]) {
                    count++;
                    dfs(i, j);
                }
            }
        }

        // Print the number of islands
        System.out.println(count);
    }

    private static void dfs(int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || seaMap[row][col] != '@' || visited[row][col]) {
            return;
        }

        visited[row][col] = true;

        // Perform DFS in all four directions
        dfs(row - 1, col); // Up
        dfs(row + 1, col); // Down
        dfs(row, col - 1); // Left
        dfs(row, col + 1); // Right
    }
}
