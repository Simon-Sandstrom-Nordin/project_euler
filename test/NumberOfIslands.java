package test;
import java.util.Scanner;   // Imports scanner class

public class NumberOfIslands {

    //function that find the number of islands
    public int findIslands(char[][] matrix)
    {
        //finds and stores the length of the matrix or grid
        int h = matrix.length;
        if (h == 0) {
            //if matrix has no elements, returns 0
            return 0;
        } else {
            int l = matrix[0].length;
            //variable to store result
            int result = 0;
            //loop iterates over rows
            for (int i = 0; i < h; i++) {
                //loop iterates over columns
                for (int j = 0; j < l; j++) {
                    if (matrix[i][j] == '@') {
                        //if the above condition returns true, calls the dfs() function and increments the result
                        dfs(matrix, i, j);
                        result++;
                    }
                }
            }
            return result;
        }
    }

    public static char[][] generateCharMatrix(int rows, int cols)
    {
        Scanner sc = new Scanner(System.in);
        char[][] matrix = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = str.charAt(j);
            }
        }
        return matrix;
    }

    //function performs the depth first search over the matrix
    public void dfs(char[][] matrix, int row, int col)
    {
        int H = matrix.length;
        int L = matrix[0].length;
        //returns true if any of the condition returns true
        if (row < 0 || col < 0 || row >= H || col >= L || matrix[row][col] != '@')
            return;
        //marking element as visited
        matrix[row][col] = '~';
        //moves in right direction
        dfs(matrix, row+ 1, col);
        //moves in left direction
        dfs(matrix, row- 1, col);
        //moves in downward direction
        dfs(matrix, row, col + 1);
        //moves in upward direction
        dfs(matrix, row, col - 1);
    }

    //driver code
    public static void main(String args[])
    {
        //creating an instance of the class
        NumberOfIslands noi = new NumberOfIslands();

        //get #rows and columns
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();

        //char matrix
        char[][] islandGrid = generateCharMatrix(rows, cols);

        //grid in which we have to find number of islands
        //char[][] islandGrid = new char[][]
         //       {
          //              {'@', '@', '~', '~', '~'},
           //             {'@', '@', '~', '~', '~'},
            //            {'~', '~', '@', '~', '~'},
             //           {'@', '~', '~', '@', '~'}};

        //prints the result
        System.out.println("Number of Islands: " + noi.findIslands(islandGrid));
    }
}
