#include <iostream>
using namespace std;

int main()
{
    int num;
    cin>>num;

    int test_5=num%5;
    int test_11=num%11;
    
    if(test_5 ==0 && test_11==0){
        cout<<"BOTH";
    }
     if((test_5 ==0 && test_11>0) || (test_5>0 && test_11==0)){
        cout<<"ONE";
    } if(test_5>0 && test_11>0){
        cout<<"NONE";
    }
}