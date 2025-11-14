#include <iostream>
using namespace std;

int main()
{
    float a,b, ave = (a + b) / 2;

    cout <<"Enter Your First Grade: ";
    cin >> a;
    cout <<"\nEnter Your Second Grade: ";
    cin >> b;
        
        cout <<"\n\nYour Average: " << ave;
        
                if (ave >= 97){
                    cout <<"\nYour Letter Grade is: A+";
                }else if (ave >= 93){
                    cout <<"\nYour Letter Grade: A";
                }else if (ave >= 90){
                    cout <<"\nYour Letter Grade: A-";
                }else if (ave >= 87){
                    cout <<"\nYour Letter Grade: B+";
                }else if (ave >= 83){
                    cout <<"\nYour Letter Grade: B";
                }else if (ave >= 80){
                    cout <<"\nYour Letter Grade: B-";
                }else if (ave >= 77){
                    cout <<"\nYour Letter Grade: C+";
                }else if (ave >= 73){
                    cout <<"\nYour Letter Grade: C";
                }else if (ave >= 70){
                    cout <<"\nYour Letter Grade: C-";
                }else if (ave >= 67){
                    cout <<"\nYour Letter Grade: D+";
                }else if (ave >= 65){
                    cout <<"\nYour Letter Grade: D";
                }else {
                    cout <<"Your Letter Grade: F";
                }
    return 0;
}