#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    vector<int> A;
	    int x;
	    for (int i=0;i<n;i++)
	    {
	        cin>>x;
	        A.push_back(x);
	    }
	    sort(A.begin(),A.end());
        vector<int> v;
        for(int i=0;i<n-1;i+=2)
        {
            v.push_back(A[i+1]);
            v.push_back(A[i]);
        }
        for(int i=0;i<n;i++) cout<<v[i]<<" ";
        cout<<endl;
	}
}
