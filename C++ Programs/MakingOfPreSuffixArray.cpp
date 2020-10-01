#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    int i,j,a[100];
    cin >> s;
    a[0]=0;
    i=1;
    j=0;
    while(i<s.length())
    {
        if(s[i]==s[j])
        {
            a[i]=j+1;
            i++;
            j++;
        }
        else
        {
            if(j==0)
            {
                a[i]=0;
                i++;
            }
            else
            {
                j=a[j-1];
            }
        }
    }
    for(i=0;i<s.length();i++)
        cout << a[i] << " ";

}
