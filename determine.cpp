#include <iostream>
using namespace std;

int main(){
    int even = 0, odd = 0, num;
    cout<<"Enter a Number: ";
    cin>>num;
    if (num %2==0){
    even++;
    cout<<"The number you entered is an even number ";
    }else{
        odd++;
        cout<<"The number you entered is an odd number";
    }

return 0;
}