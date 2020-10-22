import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Binnarytodecimal {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner k= new Scanner(System.in);
        String a= k.nextLine();
        int n= a.length();
        int x=0;
        for (int i=n-1;i>=0;i--){
            if (a.charAt(i)=='1'){
                 
                  x+= Math.pow(2,n-i-1);
            }
           
            
        }
        System.out.println(x);
        
    }
}
