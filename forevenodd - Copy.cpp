#include<iostream>
#include<cstdlib>

using namespace std;

int main()
{
    int num1, num2;
    cout<<"\nDIRECTION!!!\nThis program will show you the list of the numbers from the first number to the last number.\nThe list will depend if the first number you input is an Odd/Even number.\n";
    cout<<"The Second Number you input serves as the stopping number, it will stop even if the input numbers are not the same.\n\n";
    cout<<"===========================================\n";
    cout<<"Enter the First Number: ";
    cin>>num1;
    cout<<"Enter the Last Number: ";
    cin>>num2;

    if(num1 %2==0)
    {
        
        cout<<"The Starting number is an Even number: "<<num1<<"\n\n";
        cout<<"The list of Even numbers from "<<num1<<" to " <<num2<< " are: \n";
    }
    else
    {
        
        cout<<"The Starting number is an Odd number: "<<num1<<"\n\n";
        cout<<"The list of Odd numbers from "<<num1<<" to " <<num2<< " are: \n";
    }

    if(num1<num2)
    {
        for(num1;num1 <= num2;num1+=2)
        {
            cout<<num1<<" ";
        }
    }
    else
    {
        for(num1;num1 >= num2;num1-=2)
        {
            cout<<num1<<" ";
        }
    }
        cout<<"\n===========================================\n";

    return 0;
}