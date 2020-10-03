#include <iostream>

using namespace std;

int main()
{
    
int number;
float t,root;
cout<<"enter the number"<<"\n";
cin>>number;
root=number/2;
t=0;
while(root != t)
{
    t=root;
    root=(number/t+t)/2;
}
cout<<"root"<<"="<<root;
    return 0;

}
