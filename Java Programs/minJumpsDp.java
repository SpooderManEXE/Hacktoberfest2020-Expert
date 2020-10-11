public class minJumpsDp {
    public static void main(String[] args) {
        int[] arr = new int[]{3,2,1,0,4};
        int[] jumps_taken = new int[arr.length];
        //int[] actual_way = new int[arr.length];
        jumps_taken[0] = 0;
        //actual_way[0] = -1;
        int steps = 0;

        for(int i = 1 ; i < arr.length ; i++)
            jumps_taken[i] = Integer.MAX_VALUE-1;

        for(int i = 1 ; i < arr.length ; i++)
        {
            for(int j = 0 ; j < i ;j++)
            {
                if(j + arr[j]>= i)
                {
                    if(jumps_taken[i] > jumps_taken[j]+1)
                    {
                       // actual_way[i] = j;
                        jumps_taken[i] = jumps_taken[j] + 1;
                    }
                }
            }
        }

        System.out.print(jumps_taken[arr.length-1]);
    }
}

