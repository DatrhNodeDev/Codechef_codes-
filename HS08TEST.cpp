#include<iostream>
#include <iomanip>
using namespace std;
int main(){
    float money,bank;

    cin>>money>>bank;

    if(int(money)%5 ==0 && bank>=money+0.5)
        cout<<fixed<<setprecision(2)<<(bank-money-0.5);
    else
        cout<<fixed<<setprecision(2)<<bank;

}