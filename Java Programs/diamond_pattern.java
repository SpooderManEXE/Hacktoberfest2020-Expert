package hacktoberfest;

import java.util.Scanner;

public class diamond_pattern {
	  public static void main(String[] args) {
	        // Write your code here
	        Scanner s=new Scanner(System.in);
	        int n=s.nextInt();
	        int r=1;
	        while(r<=(n/2+1))
	        {
	        	int i=n/2;
	        	while(i>=r)
	        	{
	        		System.out.print(" ");
	        		i--;
	        	}
	        	int k=1;
	        	while(k<=((2*r)-1))
	        	{
	        		System.out.print("*");
	        		k++;
	        	}
	        	System.out.println();
	        	r++;
	        }
	        int k=1;
	        while(k<=n/2)
	        {
	        	 int d=1;
	        	 while(d<=k)
	        	 {
	        		 System.out.print(" ");
	        		 d++;
	        	 }
	        	int h=n-(2*k);int q=1;
	        	 while(q<=h)
	        	 {
	        		 System.out.print("*");
	        		 q++;
	        	 }
	        	 
	        	System.out.println();
	        	k++;
	        }
	  }
}
