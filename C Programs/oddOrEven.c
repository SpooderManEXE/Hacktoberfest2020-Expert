#include <stdio.h>

int main()
{
    printf("Enter a non-decimal number\n");
    int num;
    scanf("%d",&num);
    if(num%2==0)
        printf("Even\n");
    else 
        printf("Odd\n");
    return 0;
}
