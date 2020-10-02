#include<stdio.h> 
int fibo(int n) 
{ 
   if (n <= 1) 
      return n; 
   return fibo(n-1) + fibo(n-2); 
} 
  
int main () 
{ 
  int n;
  scanf("%d", &n);
  printf("%d", fibo(n)); 
  getchar(); 
  return 0; 
} 
