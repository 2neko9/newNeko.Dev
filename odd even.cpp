#include <iostream>
using namespace std;

int main(){
    int even = 0, odd = 0, num;
    cout<<"Enter a Number: ";
    cin>>num;
    if (num %2==0){
    even++;
    cout<<even;
    }else{
        odd++;
        cout<<odd;
    }

return 0;
}