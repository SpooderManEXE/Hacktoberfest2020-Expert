#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int a[n];
    for(int i = 0; i < n; i++)  cin >> a[i];

    sort(a, a + n);

    vector<int> v;
    v.resize(n);

    int j = 0;

    for(int i = 1; i < n; i += 2)
    {
        v[i] = a[j++];
    }
    for(int i = 0; i < n; i += 2)
    {
        v[i] = a[j++];
    }

    int ans = 0;

    for(int i = 1; i < n - 1; i++)
    {
        if(v[i] < v[i - 1] && v[i] < v[i + 1])
            ans++;
    }

    cout << ans << "\n";
    for(auto i: v)
        cout << i << " ";

    return 0;
}


