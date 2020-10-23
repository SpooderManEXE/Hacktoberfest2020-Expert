package src;

public class CC {


    public static boolean isvalid(int index, int size)
    {
        if (index < 0 || index >= size)
            return false;
        return true;
    }


    public static void dfs(int[][] A, boolean[][] visited, int row, int col, int size)
    {
        if (!isvalid(row, size) && !isvalid(col, size))
            return;

        visited[row][col] = true;

        if (isvalid(row-1, size))
        {
            if (!visited[row-1][col] && A[row-1][col] == 1)
                dfs(A, visited, row-1, col, size);
        }

        if ((isvalid(col+1, size)))
        {
            if (!visited[row][col+1] && A[row][col+1] == 1)
                dfs(A, visited, row, col+1, size);
        }

        if ((isvalid(row+1, size)))
        {
            if (!visited[row+1][col] && A[row+1][col] == 1)
                dfs(A, visited, row+1, col, size);
        }

        if ((isvalid(col-1, size)))
        {
            if (!visited[row][col-1] && A[row][col-1] == 1)
                dfs(A, visited, row, col-1, size);
        }

    }

    public static int connectedcomponents(int[][] A, boolean[][] visited, int n)
    {
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (A[i][j] == 1 && !visited[i][j])
                {
                    dfs(A, visited, i, j, n);
                    ++count;
                }
            }
        }
        return count;
    }

    public static void main(String[] args)
    {
        int[][] a = {{1,1,1,1,1,1},
                     {1,1,0,0,0,0},
                     {0,0,0,1,1,1},
                     {0,0,0,1,1,1},
                     {0,0,1,0,0,0},
                     {1,0,0,0,0,0}};
        boolean[][] visited = new boolean[6][6];
//        Arrays.fill(visited, false);
        System.out.println("Number of connected components are : " + connectedcomponents(a, visited, 6));
    }
}
