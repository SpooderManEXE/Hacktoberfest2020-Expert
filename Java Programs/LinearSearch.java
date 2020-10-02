import java.util.*;
	class LinearSearch
	{
		public static void main(String args[])
		{
		System.out.print("Enter n :");
		Scanner sc = new Scanner (System.in);
		int n = sc.nextInt();
		int arr[]=new int[n];
		System.out.println("Enter array elements :");
		for(int i=0;i<n;i++)
			arr[i] = sc.nextInt();
		System.out.print("Enter element to search for :");
		int key = sc.nextInt();
		boolean flag=false;
		for(int i=0;i<n;i++)
			if(arr[i]==key)
				flag=true;
		if(flag)
		System.out.println("Key Found!");
		else
		System.out.println("Sorry, Key Not Found!");
	}
}
