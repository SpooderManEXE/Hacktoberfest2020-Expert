#include <stdio.h>

int main()
{
    int a[100];
    int n,i,search,first,last,mid,flag=0;
    printf("Enter the number of elements in the array \n");
    scanf("%d",&n);
    printf("Enter the elements in the ascending order \n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the number to be searched \n");
    scanf("%d",&search);
    first=0;
    last=n-1;
    
    while(first<=last)
    {
        mid=(first+last)/2;
        if(a[mid]==search)
        {
            flag=1;
            break;
        }
        else if(a[mid]<search)
            first=mid+1;
        else 
            last=mid-1;
        
    }
    if(flag==1)
    {
        printf("Entered number %d is found at location %d",search,mid);
    }
    else
    {
        printf("Entered number is not found");
    }
    

    return 0;
}
