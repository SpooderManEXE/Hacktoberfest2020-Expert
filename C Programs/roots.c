#include<stdio.h>
#include<math.h>
int main()
{
 float a,b,c,d,root1,root2;
 printf("Enter a,b,c\n");
 scanf("%f%f%f,&a,&b,&c);
 d=b*b-4*a*c;
 if(d<0)
   printf("\n Imaginary roots\n);
 else
 { 
  root1=(-b+sqrt(d))/(2.0*a);
  root2=(-b-sqrt(d))/(2.0*a);
  printf("\n Root1 = %f\t\t Root2 = %f\n",root1,root2);
 }
 getchar();
 return(0);
}
