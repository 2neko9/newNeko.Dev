#include <iostream>
using namespace std;
int main(){

    char op;
    double num1, num2, sum, diff, prod, quo;
        
        cout<<"\n\n\t\tSimple Calculator\n\n";
            cout<<" Num 1: ";
            cin>>num1;
            cout<<" Operation: ";
            cin>>op;
            cout<<" Num2: ";
            cin>>num2;
                
                cout<<"\n\n Answer: \n\n";
                
                switch (op)
            {
            case '+':;
                cout<<" "<< num1<< "+" << num2<< "= " << num1 + num2; 
                break;
            case '-':;
                cout<<" "<< num1<< "-" << num2<< "= " << num1 - num2; 
                break;
            case '*':;
                cout<<" "<< num1<< "*" << num2<< "= " << num1 * num2; 
                break;
            case '/':;
                cout<<" "<< num1<< "/" << num2<< "= " << num1 / num2; 
                break;
            
            default:
                break;
            }






}