import java.util.Scanner;
	public class VowelReplace
	{	
	public static void main(String[] args)
	{		
		String a; 		
		Scanner in=new Scanner(System.in);
		System.out.println("Enter the string");
		a=in.next();
		char[] stringToCharArray = a.toCharArray();
		for (char r : stringToCharArray) 
		{
			if(r=='A'||r=='a'||r=='e'||r=='E'||r=='I'||r=='i'||r=='o'||r=='O'||	r=='u'||r=='U')
			{
				r='*';
				System.out.print(r);				
			}
			else
			{
				System.out.print(r);
			}
		}
		System.out.println();	
	}
  }
