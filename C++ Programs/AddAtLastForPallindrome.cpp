#include<bits/stdc++.h>
using namespace std;

int main(){

     int t;
     cout<<"Enter No of test cases "<<endl;
     cin>>t;
     while(t--)
     {
        cout<<"Enter a string : "<< endl;
        string A;
        getline(cin,A);
         while (A.length()==0 )
            getline(cin, A);
        int s=0, e=A.size()-1, added=0;
        while(s<=e)
        {
            if(A[s]==A[e]){s++; e--;}
            else
            {
                s++;
                e=A.size()-1;
                added=s;
            }
        }
        cout<<"No of values to be added: "<<added<<endl;
     }
}
