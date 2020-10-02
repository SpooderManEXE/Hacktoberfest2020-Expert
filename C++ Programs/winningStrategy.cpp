#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
    ll T, N;
    cin>>T;

    while(T--){
        cin>>N;
        ll A[N];
        ll c1=0, c2=0;
        for(int i = 0; i<N; i++){
            cin>>A[i];
        }
        sort(A,A+N,greater<int>());

        for(int i = 0; i<N; i++){
            if (i==0){c1+=A[i];}
            else if(i==1){c2+=A[i];}
            else if(i%2==0){
                c2+=A[i];
            }
            else if(i%2!=0){
                c1+=A[i];
            }
        }

        if(c1>c2){cout<<"first\n";}
        else if(c2>c1){cout<<"second\n";}
        else if(c2==c1){cout<<"draw\n";}

    }
    return 0;
}