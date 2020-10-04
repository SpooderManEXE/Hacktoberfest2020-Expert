#include <stdio.h>
#include <stdlib.h>
int main(void){
  int num1,num2,sum;
  printf('Enter 2 numbers:');
  scanf('%d%d',&num1,&num2);
  sum = num1 + num2;
  printf('Result is: %d',sum);
  return EXIT_SUCCESS;
}
