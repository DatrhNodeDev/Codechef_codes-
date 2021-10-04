#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int arr[n]={0};
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int ans=0;
        ans=n*(n-1);
        unordered_map<int,int>m;
        for(int i=0;i<n;i++)
        {
            m[arr[i]]++;
        }
        for(auto it: m)
        {
            int count=it.second;
            if(count>=2)
            {
                ans=ans-(count*(count-1));
            }
        }
        cout<<ans<<endl;
    }
}
