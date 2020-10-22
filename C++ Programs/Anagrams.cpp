#include<bits/stdc++.h>
using namespace std;

int main(){

     int t;
     cout<<"Enter No of test cases "<<endl;
     cin>>t;
     while(t--)
     {
        int n;
        cout<<"Enter no of words "<<endl;
        cin>>n;
        vector<string> A; // To store words
        for (int i=0; i<n;i++) {
            string s;
            cout<<"Enter word at index  : " <<  i+1 <<endl;
            cin>>s;
            A.push_back(s);
        }
        vector<vector<int> > v; // To store the index of words which are Anangrams
        vector<int> temp;
        vector<string> q;
        unordered_map<string ,vector<int> > m;
        for(int i=0;i<A.size();i++)
        {
            string temp=A[i];
            sort(temp.begin(),temp.end());
            q.push_back(temp);
        }
        for(int i=0;i<q.size();i++)
        {
            m[q[i]].push_back(i+1);
        }
        for(auto i=m.begin();i!=m.end();i++)
        {
            v.push_back(i->second);
        }
        for ( int i=0;i<v.size();i++)
        {
            cout<<"[ ";
            for(int j=0;j<v[i].size();j++)
            {
                cout<<v[i][j]<<" ";
            }
            cout<<"]";
        }
        cout<<endl;
    }
} // The index displayed in [] forms anagram of each other 
