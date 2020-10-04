#include<stdio.h>
#include<stdlib.h>
void main()
{
    float mrk;
    printf("\nEnter the mark\n");
    scanf("%f",&mrk);

    if (mrk>=90)
        printf("\nGrade = A\n");
    else if ((mrk>=80) && (mrk<90))
        printf("\nGrade= B+\n");
    else if ((mrk>=70) && (mrk<80))
        printf("\nGRADE= B\n");
    else if ((mrk>=60) && (mrk<70))
        printf("\nGRADE= C+\n");
    else if ((mrk>=50) && (mrk<60))
        printf("\nGRADE= C");
    else
    {
     printf("\nFAIL\n GRADE= F\n");
    }
}
    
