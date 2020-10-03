#include<stdio.h>
#include<stdlib.h>

void main(){
	int i,num;
	printf("\nEnter number of random digits:");
	scanf("%d",&num);
	
	for(i=0;i<num;i++){
		printf("%d\n",rand()%num);
	}
}
