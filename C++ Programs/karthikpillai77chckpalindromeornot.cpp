#include <iostream> 
#include<string.h> 
using namespace std; 
void m(char[]);
int main()
{ 
    char string[30]; 
    cout << "Enter the string"<<"\n";  
    cin >> string; 
    m(string);
    return 0;     
}
void m(char k[])
{
    int flag;
    flag=0;
    int length,i;
    length = strlen(k); 
    for(i=0;i<length;i++)
    { 
        if(k[i] != k[length-i-1])
{ 
          flag = 1;
           break; 
   } 
}
if (flag) { 
        cout << k << " is not a palindrome" <<"\n";  
    }     
    else { 
        cout << k << " is a palindrome" <<"\n";  
    } 
}
