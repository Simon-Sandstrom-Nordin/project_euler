package test.java_tasks;
import java.util.BitSet;
import java.util.Scanner;

public class IslandCounter {

    // global variables? Public/private attributes? idk java.
    private int rows;
    private int cols;
    private BitSet visited;

    public int countIslands(char[][] seaMap) {
        rows = seaMap.length;
        cols = seaMap[0].length;
        visited = new BitSet(rows * cols);
        int count = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (seaMap[i][j] == '@' && !visited.get(i * cols + j)) {
                    count++;
                    exploreIsland(seaMap, i, j);
                }
            }
        }

        return count;
    }


    // rekursiv metod för att djupet först söka efter grannöar
    private void exploreIsland(char[][] seaMap, int row, int col) {
        if (!isValidPosition(row, col)) // kommer utanför kartan
            return;

        if (seaMap[row][col] == '@' && !visited.get(row * cols + col)) {
            visited.set(row * cols + col);
            exploreIsland(seaMap, row - 1, col); // Upp
            exploreIsland(seaMap, row + 1, col); // Ner
            exploreIsland(seaMap, row, col - 1); // Vänster
            exploreIsland(seaMap, row, col + 1); // Höger
        }
    }

    private boolean isValidPosition(int row, int col) {
        return row >= 0 && row < rows && col >= 0 && col < cols;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // antal tecken per column
        int x = scanner.nextInt();
        // antal tecken per rad
        int y = scanner.nextInt();

        char[][] seaMap = new char[x][y];

        // enter sea map row by row
        for (int i = 0; i < x; i++) {
            String row = scanner.next();
            seaMap[i] = row.toCharArray();
        }

        IslandCounter islandCounter = new IslandCounter();
        int result = islandCounter.countIslands(seaMap);
        // print number of islands
        System.out.println(result);
    }
}
