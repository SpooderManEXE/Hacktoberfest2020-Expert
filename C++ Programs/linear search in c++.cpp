#include<iostream>
using namespace std;
main(){
	int a[20],n,i,search,pos,value;
	cout<<"enter size of array";
	cin>>n;
	cout<<"enter array elements";
	for(i=0;i<n;i++){
		cin>>a[i];
	}
	cout<<"enter the value to be searched";
	cin>>value;
	search=a[0];
	if(value==search){
		cout<<"found at 1st position";
	}
	else{
	for(i=1;i<n;i++){
	if(value==a[i])
	{
		search=a[i];
		pos=i+1;
		cout<<"found at "<<pos<<"th position";
		break;
		}	
		else{
			continue;
		}
	}
}
if(search!=value){
	cout<<"Value not found";
}
return 0;
}
