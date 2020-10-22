#include<bits/stdc++.h>
using namespace std;

int main(){

     int t;
     cout<<"Enter No of test cases "<<endl;
     cin>>t;
     while(t--)
     {
        cout<<"Enter a string (You can enter spaces in between words as well as in the end and front)"<<endl;
        string A;
        getline(cin,A);
         while (A.length()==0 ) // This ensures that a blank string wont be counted as a test case
            getline(cin, A);
         string temp="";
        int count=0;
        for(int i=0;i<A.length();i++)
        {
            if(A[i]!=' ')
            {
                temp+=A[i];
                count=temp.length();
            }
            else if(A[i]==' ') temp="";
        }
        if(A[A.length()-1]!=' ') count=temp.length();
        cout<<"Length of the last word : " << temp<< " " << count<<endl;
     }
}
