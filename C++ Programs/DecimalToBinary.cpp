//this C++ program converts a decimal number into a binary number

#include<bits/stdc++.h>

using namespace std;

int main()
{
    int decimal;
    cout<<"Enter a decimal number to covert into binary number: ";
    cin>>decimal;

    int temp = decimal;
    int binary = 0;
    int i=1;

    for(int j = temp; j>0; j/=2)
    {
        binary += (temp%2)*i;
        i *= 10;
        temp /= 2;
    }

    cout<<decimal<<" in binary: "<<binary;
    return 0;
}
