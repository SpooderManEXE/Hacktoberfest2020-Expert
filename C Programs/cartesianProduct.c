// Cartesian Product
#include <stdio.h>

int cartesian(int a[20], int b[20], int m, int n)
{
    printf("Cartesian Product of two sets:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("{ %d, %d } ", a[i], b[j]);
        }
    }
}

int main()
{
    int a[20], b[20], m, n;

    printf("\nEnter number of elements in 1st set:\n");
    scanf("%d", &n);

    printf("Enter number of elements in 2nd set:\n");
    scanf("%d", &m);

    printf("Enter the elements of 1st set:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Enter the elements of 2nd set:\n");
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &b[i]);
    }

    cartesian(a, b, m, n);

    return 0;
}
/* OUTPUT
    Enter number of elements in 1st set:
    3
    Enter number of elements in 2nd set:
    4
    Enter the elements of 1st set:
    1 2 3
    Enter the elements of 2nd set:
    7 8 9 10
    Cartesian Product of two sets:
    { 1, 7 } { 1, 8 } { 1, 9 } { 1, 10 } { 2, 7 } { 2, 8 } { 2, 9 } { 2, 10 } { 3, 7 } 
    { 3, 8 } { 3, 9 } { 3, 10 }
*/