#include<iostream>
using namespace std;
main(){
	int a[100],pos,data,n,i;
	cout<<"enter the size of array";
	cin>>n;
	cout<<"enter array elements";
	for(i=0;i<n;i++){
		cin>>a[i];
	}
	cout<<"enter the index where an element should be inserted";
	cin>>pos;
	cout<<"enter the data u want to insert";
	cin>>data;
	for(i=n-1;i>=pos;i--){
		a[i+1]=a[i];
	}
	a[pos]=data;
	n=n+1;
	cout<<"updated Array is :"<<endl;
	for(i=0;i<n;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}
