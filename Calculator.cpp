#include <iostream>
using namespace std;

int main(){
char operation;
double num1, num2, sum, prod, dif, quo;

        cout<<"\n\n\t\t\t Calculator\n\n";
        
        cout<<" What Operation do you want: ";
            cin>>operation;
        cout<<"--> ";
            cin>>num1;
        cout<<"--> ";
            cin>>num2;
        
        cout<<"----------\n";
        
        switch (operation)
        {
        case '+':;
            sum = num1 + num2;
            cout<<"= "<< sum <<"\n\n";
            break;
            
        case '-':;
            dif = num1 - num2;
            cout<<"= "<< dif <<"\n\n";
            break;
        
        case '*':;
            prod = num1 * num2;
            cout<<"= "<< prod <<"\n\n";
            break;
            
        case '/':;
            quo = num1 / num2;
            cout<<"= "<< quo <<"\n\n";
            break;
            
            default:
            cout<<" Error \n\n";
            break;
        
        
        }

return 0;
}