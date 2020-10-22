#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 
  
int main() 
{ 
    // declaring argument of time() 
    time_t my_time = time(NULL); 
  
    // ctime() used to give the present time 
    printf("%s", ctime(&my_time)); 
    return 0; 
}
