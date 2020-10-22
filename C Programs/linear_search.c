#include <stdio.h>
int main()
{
    int i,num,a[100],l,flag=0;
    printf("Enter the length of array: ");
    scanf("%d",&l);
    printf("enter the elements\n");
    for(i=0;i<l;i++)
        scanf("%d",&a[i]);
    
    printf("enter the number you want to find: ");
    scanf("%d",&num);
    for(i=0;i<l;i++){
        if(a[i]==num){
        flag = 1;
        break;
        }
    }
    if(flag == 1)
    printf("the number %d is in position %d",num,i+1);
    else
    printf("the number %d is not found",num);
    return 0;
}
