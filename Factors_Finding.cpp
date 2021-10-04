#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
    int x;
    cin>>x;
    int fac_cnt=0;
    
    vector<int> arr;
    for (int i =1;i<pow(x,0.5)+1;i++)
    {
      
        if(x%i==0)
        {
            arr.push_back(i);
        }
    }

    arr.push_back(x);

    cout<<arr.size()<<endl;
    for (auto i = arr.begin(); i != arr.end(); ++i)
        cout << *i << " ";
}