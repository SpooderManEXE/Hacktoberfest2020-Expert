#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    char str[200];
    int i=0, wrd=1;	
    printf("Input the string : ");
    fgets(str, sizeof str, stdin);	
    while(str[i]!='\0')
    {        if(str[i]==' ' || str[i]=='\n' || str[i]=='\t')
        {
            wrd++;
        }
        i++;
    }
    printf("Total number of words in the string is : %d\n", wrd-1);
    getchar();
    return(0);
}
