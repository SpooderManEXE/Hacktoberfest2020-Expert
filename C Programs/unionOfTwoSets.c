// Union of two sets

int unionS(int a[], int b[], int n, int m)
{
    int k = 0, flag, u[40];

    for (int i = 0; i < n; i++)
    {
        u[k] = a[i];
        k++;
    }
    for (int i = 0; i < m; i++)
    {
        flag = 0;
        for (int j = 0; j < n; j++)
        {
            if (b[i] == a[j])
                flag = 1;
        }
        if (flag == 0)
        {
            u[k] = b[i];
            k++;
        }
    }

    for (int i = 0; i < k; i++)
    {
        printf("%d ", u[i]);
    }
}

#include <stdio.h>

int main()
{
    int a[20], b[20], n, m, i, j;

    printf("Enter number of elements in 1st set:\n");
    scanf("%d", &n);

    printf("Enter number of elements in 2nd set:\n");
    scanf("%d", &m);

    printf("Enter the elements:\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Enter the elements:\n");
    for (i = 0; i < m; i++)
    {
        scanf("%d", &b[i]);
    }
    unionS(a, b, m, n);

    return 0;
}