public class Main
{
	public static void main(String[] args) {
		int[][] a = {{1,2,3},{4,5,6},{7,8,9}};
		int[][] b = {{11,12,13},{14,15,16},{17,18,19}};
		int i,j;
		System.out.println("Array A:");
        for(i=0;i<3;i++){
            for(j=0;j<3;j++)
                System.out.print(a[i][j] + " ");
            System.out.println();
        }        
        System.out.println("Array B:");
        for(i=0;i<3;i++){
            for(j=0;j<3;j++)
                System.out.print(b[i][j] + " ");
            System.out.println();
        }
        System.out.println("\nArray A + Array B:");
        for(i=0;i<3;i++){
            for(j=0;j<3;j++)
                System.out.print(b[i][j] + a[i][j] + " ");
            System.out.println();
	}
	}	
}
