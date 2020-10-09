#include <stdio.h>

void and ()
{
    int a[2][2], i, j;

    printf("\n\nAND(&&) Gate:\n");
    printf("A.B : A&&B\n");
    for (i = 0; i <= 1; i++)
    {
        for (j = 0; j <= 1; j++)
        {
            a[i][j] = (i && j);
            printf("%d.%d : %d\n", i, j, a[i][j]);
        }
    }
}

void or ()
{
    int b[2][2], i, j;

    printf("\n\nOR(||) Gate: \n");
    printf("A+B : A||B\n");
    for (i = 0; i <= 1; i++)
    {
        for (j = 0; j <= 1; j++)
        {
            b[i][j] = (i || j);
            printf("%d+%d : %d\n", i, j, b[i][j]);
        }
    }
}

void not()
{
    int c[2], i;
    printf("\n\nNOT Gate (!)\n");
    printf("A : B=!A\n");
    for (int i = 0; i <= 1; i++)
    {
        c[i] = (!i);
        printf("%d : %d\n", i, c[i]);
    }
}

int main()
{
    int ch=0;
    
    printf("\n\nEnter 1 for AND operation\n");
    printf("Enter 2 for OR operation\n");
    printf("Enter 3 for NOT operation\n");
    printf("Enter 4 to EXIT\n");

    while (ch < 4)
    {

        scanf("%d", &ch);

        switch (ch)
        {
        case 1:
            and();
            break;
        case 2:
            or ();
            break;
        case 3:
            not();
            break;
        case 4:
            exit(0);
        default: 
            printf("WRONG CHOICE !!!!");
            break;
        }
    }

    return 0;
}


/*OUTPUT
Enter 1 for AND operation
Enter 2 for OR operation 
Enter 3 for NOT operation
Enter 4 to EXIT
1


AND(&&) Gate:
A.B : A&&B   
0.0 : 0      
0.1 : 0      
1.0 : 0      
1.1 : 1      

2


OR(||) Gate: 
A+B : A||B   
0+0 : 0
0+1 : 1
1+0 : 1
1+1 : 1

3


NOT Gate (!)
A : B=!A
0 : 1
1 : 0

*/