import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Average {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner k= new Scanner(System.in);
        System.out.println("enter the Size of the array"); 
        int n = k.nextInt();
        float []a= new float[n];
        float x=0;
        float avg;
        System.out.println("Enter the elements of the array ");
        for (int i=0;i<n;i++){
            a[i]=k.nextFloat();
        }
        for (int i=0;i<n;i++){
            x=x+ a[i];
        }
        avg=x/n;
        System.out.printf(" Average of the elements in the array is :%.1f",avg);
    }
}
