package rec3;

public class merge_sort {
	
	public static void mergeSort(int[] input){
		
        sort(input , 0, input.length-1);
		
	}
    
      
    public static void merge(int input[], int beg, int mid, int end){  
  
        int l = mid - beg + 1;  
        int r = end - mid;  
  
        int LA[] = new int [l];  
        int RA[] = new int [r];  
  
        for (int i=0; i<l; i++)  
             LA[i] = input[beg + i];  
  
        for (int j=0; j<r; j++)  
             RA[j] = input[mid + 1+ j];  
        
        int i = 0, j = 0;  
        int k = beg;  
         
        while (i<l&&j<r)  
        {  
            if (LA[i] <= RA[j])  
            {  
                input[k] =LA[i];  
                i++;  
            }  
            else  
            {  
                input[k] = RA[j];  
                j++;  
            }  
            k++;  
        }  
        
        while (i<l)  
        {
            input[k] = LA[i];  
            i++;  
            k++;  
        }  
  
        while (j<r)  
        {  
            input[k] = RA[j];  
            j++;  
            k++;  
        }  
    }  
  
    static void sort(int input[], int p, int r)  
    {  
        if (p<r)  
        {  
            int q = (p+r)/2;  
            sort(input, p,q);  
            sort(input , q+1, r);  
            merge(input, p, q, r); 
        }  
    }  

	
	public static void main(String[] args)
	{
		int input[]= {2,1,5,2,3};
		sort(input,0,input.length-1);
		for(int i=0;i<input.length;i++)
		{
			System.out.print(input[i]+" ");
		}
	}

}
