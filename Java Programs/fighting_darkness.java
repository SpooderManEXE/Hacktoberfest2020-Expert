package programs;

public class fighting_darkness {
	
	public static long maxdays(int arr[],int n)
	{
		int count=0;
		for(int i=0;i<arr.length;i++)
		{
			if(arr[i]<=n)
			{
				if(count<arr[i])
				{
				count=arr[i];
				}
			}
		}
		return count;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int n=5;
int arr[]= {2,3,4,2,1};
     long ans=maxdays(arr, n);
     System.out.println(ans);
	}

}
