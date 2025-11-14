#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    int x, i ;
    double sub1, sub2, sub3, sub4, sub5, qnty, total,cash;
    double price[6] = {0, 50.00, 25.00, 20.00, 80.00, 60.00};
    string menu[6] = {""," [1] Hamburger\t\t\tPhp 50.00", " [2] Fries\t\t\tPhp 25.00", " [3] Softdrinks\t\t\tPhp 20.00", " [4] Chicken with Rice\t\tPhp 80.00", " [5] Hotdog with Rice\t\tPhp 60.00" };
    string menu2[6] = {"","Hamburger\t\t\tPhp 50.00", "Fries\t\t\tPhp 25.00", "Softdrinks\t\t\tPhp 20.00", "Chicken with Rice\t\tPhp 80.00", "Hotdog with Rice\t\tPhp 60.00" };
    
    cout<<"\n\n\t\tNeil's FastFood\n";
    cout<<"\n\t\t    Menu's:\n";
            
    for( i = 1; i < 6; i++){
    cout<<menu[i]<<"\n";
    }
                    
    cout<<"\n\n How many Orders do you want: ";
    cin>>x;
    if(x > 5){
        cout<<"\nThe Order Limit is 5!!!";
    return 0;
    }
    int *myarray = new int(x); 
    int *myarray2 = new int(x);
    cout<<" What is your meal:) \n\n";
                        
    for(i =1; i < x+1; i++){
                                                
        cout<<" Order #"<<i<<": ";
            cin>>myarray[i];
        cout<<" How many: ";
            cin>>myarray2[i];
        cout<<"\n";
        }
                                                    
        cout<<"\n\n\t\t\tYour Orders:\n\n";
            for(i=1; i < x+1; i++){
                if(myarray[i] < 6){
                cout<<" Order #"<<i<<": "<< menu2[myarray[i]]<<" X "<< myarray2[i] << " = "<< myarray2[i] * price[myarray[i]]<<"\n";
                }else if (myarray[i] > 5){
                cout<<" Your Order isn't on the menu.\n";
                }else if (myarray[i] < 1){
                cout<<" Your Order isn't on the menu.\n";
                }
                                                }
        for(i = 1; i < x+1; i++){
        if(myarray[i] == 1){
            sub1 += 50.00 * myarray2[i];
        } else if(myarray[i] == 2){
            sub2 += 25.00 * myarray2[i];
        } else if(myarray[i] == 3){
            sub3 += 20.00 * myarray2[i];
        } else if(myarray[i] == 4){
            sub4 += 80.00 * myarray2[i];
        } else if(myarray[i] == 5){
            sub5 += 60.00 * myarray2[i];
        }
        }
            total = sub1 + sub2 + sub3 + sub4 + sub5;
            cout<<"\n Total Amount is: "<<"Php "<<total<<"\n";
                    
            cout<<" Your Cash: Php "; 
                cin>>cash;
                
            if(cash < total){
                cout<<" You don't have enough Money!!!\n\n";
                } else if (cash >= total){
            cout<<"\n Change: Php "<< cash - total<<"\n\n";
            cout<<"\t\tThank you, Come Again\n\n";}
        
    
return 0;
}