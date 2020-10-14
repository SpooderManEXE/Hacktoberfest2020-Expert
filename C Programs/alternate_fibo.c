/*It is a program to print the alternate fibonacci numbers upto n terms*/
#include<stdio.h>
int main()
{
	int x=0, y=1, temp, i, n;
		printf("Enter the last number\n");
		scanf("%d",&n);
	for(i=0;temp<=n;i++)
	{
	if(i==0)
	printf("%d",x);
	temp=x+y;
	x=y;
	y=temp;
	if(i%2==0)
	printf("\t%d",temp);	
	}
	return 0;
}
