// Power Set
#include <stdio.h>
#include <math.h>

int powerSet(int arr[], int n)
{
    int count = pow(2, n);
    for (int i = 0; i < count; i++)
    {   
        printf("{ ");
        for (int j = 0; j < n; j++)
        {
            if ((i & (1 << j)) != 0)
            printf("%d", arr[j]);
        }
        printf(" } ");
    }
}

int main()
{
    int n;

    printf("\nEnter size of the set\n");
    scanf("%d", &n);

    int arr[n];
    printf("Enter elements of the set\n");
    for (int i = 0; i < n; i++){ scanf("%d", &arr[i]); }

    printf("Power Set : {  ");
    powerSet(arr, n);
    printf(" }");

    return 0;
}
/* OUTPUT
    Enter size of the set
    3
    Enter elements of the set
    1
    2
    3
    Power Set : {  {  } { 1 } { 2 } { 12 } { 3 } { 13 } { 23 } { 123 }  }  
*/