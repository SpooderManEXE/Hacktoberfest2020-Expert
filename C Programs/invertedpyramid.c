#include <stdio.h>
void main() {
    int i,j,k;
    for(i=7;i>=1;i--)
    {
        for(j=7;j>i;j--)
        {
            printf(" ");
        }
        for(k=1;k<=i;k++)
        {
            printf("*");
        }

    printf("\n");
    }
}
