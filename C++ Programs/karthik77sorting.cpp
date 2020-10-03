#include<iostream>
using namespace std;

int main()
{
    int n,j,k,i,temp, flag;
    
    cout<<"enter the size of the array"<<"\n";
    cin>>n;
    int a[n];
    cout<<"enter the elements"<<"\n";
    i=0;
    while(i<n)
    {
        cin>>a[i];
        i=i+1;
    }
    cout<<"The elements before sorting"<<"\n";
    i=0;
    while(i<n)
    {
        cout<<a[i]<<"\n";
        i=i+1;
        
    }
    i=0;
    while(i<n-1)
    
      {
          flag=0;
          i=i+1;
          j=0;
    while(j<n-1)
    {
        if(a[j]>a[j+1])
        {
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
       
        }
        j=j+1;
    if(flag=0)
    break;
    }
      }
      cout<<"The elements after sorting"<<"\n";
    i=0;
    while(i<n)
    {
        cout<<a[i]<<"\n";
        i=i+1;
    }
    return 0;
    }
