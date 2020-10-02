#include<iostream>
using namespace std;
void sorting(int arr[],int n)
{
	int i, j;
	for (i = 0; i < n; ++i)
	{
		for (j = 0; j < n-i-1; ++j)
		{
			if (arr[j] > arr[j+1])
			{
				arr[j] = arr[j]+arr[j+1];
				arr[j+1] = arr[j]-arr[j + 1];
				arr[j] = arr[j]-arr[j + 1];
			}
		}
	}	
	cout<<"\n After sorting : ";
	for (i = 0; i < n; i++)
	{
		cout<<arr[i]<<"\t";
	}			
}
int main()
{
	int size;
	int k[size];
	cout<<"Enter the size : ";
	cin>>size;
	for(int i=0;i<size;i++)
	{
		cout<<"\n Enter the number : ";
		cin>>k[i];
	}
	sorting(k,size);
	return 0;
}
