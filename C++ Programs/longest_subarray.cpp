#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
int n; cin>>n;
int a[n];
for(int i=0;i<n;i++){ 
    cin>>a[i];
}
int cnt=0;
int max=0;
for(int i=0;i<n;i++)
{ 
    if(a[i]>=0)
   {
      cnt++;
   }
    else
   {
         if(cnt>max)
         {
             max=cnt;
         }
    cnt=0;
   }
}
if(cnt>max)
{
max=cnt;
}
cout<<max<<endl; 

} 
