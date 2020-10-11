#include<iostream>
using namespace std;
int main(){
	int a[100],i,j,n,min,temp;
	cout<<"enter size";
	cin>>n;
	cout<<"enter array";
	for(i=0;i<n;i++){
		cin>>a[i];
	}
	for(i=0;i<n-1;i++){
		min=i;
		for(j=i+1;j<n;j++){
			if(a[j]<a[min]){
				temp=a[min];
				a[min]=a[j];
				a[j]=temp;
			}
		}
	}
	cout<<"Sorted array is :";
	for(i=0;i<n;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}
