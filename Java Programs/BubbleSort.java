import java.lang.*;
	import java.util.*;

	public class BubbleSort{
	public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the size of the array");
            int n = sc.nextInt();
            int i;
            int []a = new int[n];
            System.out.println("Enter the array elements");
            for(i=0;i<a.length;i++){
                a[i] = sc.nextInt();
            }
            Sort s = new Sort();
            s.sort(a);
            s.print(a);
        }
}

	class Sort{
   	 void sort(int []a){
        int i, j, temp;
        for(i=0;i<a.length-1;i++){
            for(j=0;j<a.length-1-i;j++){
                if(a[j]>a[j+1])
                {
                    temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }
    }
    void print(int []a){
        for(int i=0;i<a.length;i++){
            System.out.println(a[i] + "  ");
        }
    }
}
