using System;  
                  
public class LinearSearch  
{  
    public static void Main()  
    {  
    int[] arr = {16, 19, 20, 23, 45, 56, 78, 90, 96, 100};  
    int location=-1;   
    Console.WriteLine("Enter the item which you want to search ");  
    int item = Convert.ToInt32(Console.ReadLine());  
    location = binarySearch(arr, 0, 9, item);  
    if(location != -1)   
    {  
        Console.WriteLine("Item found at location "+ location);  
    }  
    else  
    {  
        Console.WriteLine("Item not found");  
    }  
}   
public static int binarySearch(int[] a, int beg, int end, int item)  
{  
    int mid;  
    if(end >= beg)   
    {     
        mid = (beg + end)/2;  
        if(a[mid] == item)  
        {  
            return mid+1;  
        }  
        else if(a[mid] < item)   
        {  
            return binarySearch(a,mid+1,end,item);  
        }  
        else   
        {  
            return binarySearch(a,beg,mid-1,item);  
        }  
      
    }  
    return -1;   
  
    }  
}  
