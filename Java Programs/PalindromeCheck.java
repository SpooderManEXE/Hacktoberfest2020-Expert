import java.util.Scanner;
	public class PalindromeCheck{
    	public static void main(String []args){
    	    Scanner sc=new Scanner(System.in);
    	    System.out.println("Enter the string");
      	  String str=sc.next();
      	  char ch[]=new char[str.length()];
      	  for(int i=0;i<str.length();i++)
        	    ch[i]=str.charAt(str.length()-i-1);
      	  String str1=new String(ch);
      	  if(str.equals(str1))
      	      System.out.println("The string is a palindrome");
     	   else
      	      System.out.println("The string is not a palindrome");
  	  }
	}
