#include <iostream>
using namespace std;
void multiple(int);         
int main()
{
    int n1;
    cout<<"Enter the number"<<"\n";
    cin>>n1;
    multiple(n1);
    return 0;
}
void multiple(int a)           
{
    if(a%2==0)
    cout<<" It is a even number";
    else
    cout<<" It is a odd number";                     
}

