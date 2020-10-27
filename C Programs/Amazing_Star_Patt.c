#include <stdio.h>

#include <stdlib.h>

#include <math.h>

int main()

{ float n,i,j,q,w;

q=tan(M_PI*0.4);

w=tan(M_PI*0.2);

printf("Enter the size\n");

scanf("%f",&n);

for(j=ceil(n*q);j>=0;j--){

for(i=-ceil(0.55*n*q/w-n);i<ceil(0.55*n*q/w-n);i+=0.6){

if((j<=0.55*n*q && j>=(i+n)*w && j>=(n-i)*w)||(j>=(i+n)*w && j<=(i+n)*q && j<=(n-i)*q)||(j<=(n-i)*q && j>=(n-i)*w && j<=(i+n)*q)){

printf("*");

}

else{

printf(" ");

}

}

printf("\n");

}

return 0;

}
