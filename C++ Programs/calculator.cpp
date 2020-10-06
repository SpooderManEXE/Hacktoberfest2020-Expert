#include<iostream>
using namespace std;
int main(){
	float n1,n2;
	char op;
	cout<<"Enter the two numbers";
	cin>>n1>>n2;
	cout<<"enter operation";
	cin>>op;
	switch(op){
	case '+': cout<<n1+n2;
	break;
		case '-': cout<<n1-n2;
	break;
		case '*': cout<<n1*n2;
	break;
		case '/': cout<<n1/n2;
	break;
	default:
		cout<<"Enter valid operator";
}
	return 0;
	
}
