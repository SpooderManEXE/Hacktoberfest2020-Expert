#include<bits/stdc++.h>
using namespace std;

int main(){

     int t;
     cout<<"Enter No of test cases "<<endl;
     cin>>t;
     while(t--)
     {
        int n;
        cout<<"Enter No of Rows"<<endl;
        cin>>n;
        vector<vector<int> > result(n);
        for(int i=0;i<n;i++)
            {
                result[i].resize(i+1);
                result[i][0]=result[i][i]=1;
                for(int j=1;j<i;j++)
                    {
                        result[i][j]=result[i-1][j-1]+result[i-1][j];
                    }
            }
            cout<<"["<<endl;
        for (int i=0;i<result.size();i++)
        {
            cout<<"[ ";
            for(int j=0;j<result[i].size();j++)
            {
                cout<<result[i][j]<<" ";
            }
            cout<<"]";
            cout<<endl;
        }
        cout<<"]"<<endl;
     }
}
        
