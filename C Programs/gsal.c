#include<stdio.h>

int main() {

float b;
float g;
float hra;
float da; 



printf("enter base salary:");
scanf("%f", &b);

if(b<10000)
{
    da = 0.6b ;
    hra = 0.25b ;
    g = b + da + hra;
    printf("the gross salary is: %f ",g);
}

else if(b<20000)
{
    da = 0.4*b;
    hra = 2000 ;
    g = b + da + hra;
    printf("the gross salary is: %f",g);
}


return 0;

}
