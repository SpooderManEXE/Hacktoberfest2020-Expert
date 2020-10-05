#include<iostream>
using namespace std;
int firstOcc(int a[], int n, int key){
    int s=0, e=n-1;
    int mid;
    int ans=-1;
    while(s<=e){
        mid= (s+e)/2;
        if(a[mid]==key){
           ans=mid;
            e=mid-1;
        }
        else if(a[mid]>key){
            e=mid-1;
        }
        else{
            s=mid+1;
        }
    }
    return ans;
}
int main()
{
    int a[]= {1,2,3,2,4,5,4,8};
    int n=sizeof(a)/sizeof(int);
    int key;
    cin>>key;
    int ans= firstOcc(a,n,key);
    cout<<"First Occurrence of key is "<<ans<<endl;
    
}