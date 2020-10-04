public class secondlargest
{
public static int answer(int a[])
{  
    int smallest = Integer.MAX_VALUE;
    int secondsmallest = Integer.MAX_VALUE;
    for(int i=0;i<a.length;i++)
    {
        if(a[i]<smallest)
        {
            secondsmallest=smallest;
            smallest=a[i];
            }
            if(a[i]<secondsmallest && a[i]>smallest)
            {
                secondsmallest=a[i];
            }
    }
            return secondsmallest;
    
}
	public static void main(String[] args) {
		int a[]={10,18,-8,2,22,5};
		int result = answer(a);
		System.out.println("Second smallest number of the given array is "+result );
	}
}
