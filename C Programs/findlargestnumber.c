#include <stdio.h>
int main() {
    int x, y, z;
    printf("enter first number x:");
    scanf("%d",&x);
    printf("enter second number:");
    scanf("%d",&y);
    printf("enter third number:");
    scanf("%d",&z);

    if(x>=y){
        if(x>=z){
        printf("%d is the largest number",x);
                }
        else{
            printf("%d is the largest number",z);
            }
    }
    else{
        if(y>=z){
            printf("%d is the largest number",y);
        }
        else{
            printf("%d is the largest number",z);

        }
    }
    return 0;
}
