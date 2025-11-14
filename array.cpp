#include<iostream>
using namespace std;

int main(){
    
    int num[11] = {8,2,3,4,0,4,0,2,4,0,5};
    
    int i, count=0;
    int n = 11;
    
    
    for(i = 0; i < n; i++){
        if(num[i] > 0){
            num[count++] = num[i];
        }
    }
    while(count < n){
        num[count++] = 0;
    }
    
    for(i = 0; i < n; i++ ){
        cout<<" "<< num[i];
    }
    
    return 0;
}