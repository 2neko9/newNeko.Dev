#include <iostream>
using namespace std;

int main()
{
    string fname, mname, lname, nationality, fullname, country, city, prov, bmonth;
    int grades, byear, year, age, birthday, bday, address, fgrade, sgrade;
    float ave, num1, num2, sum, dif, prod, quot;
    char op;
    // a = 95, b = 85, c = 75;
            
            cout<<"\n\n Personal Information";
            cout<< " \n Fill up the Following:";
                
                
                cout<<" \n\nEnter your Firstname: ";
                    getline(cin, fname);
                cout<<" \nEnter your Middlename: ";
                    cin >> mname;
                cout<<" \nEnter your Lastname: ";
                    cin >> lname;
                cout<<" \nEnter your Country: ";
                    cin >> country;
                cout<<" \nEnter your Province: ";
                    cin >> prov;
                cout<<" \nEnter your City: ";
                    cin >> city;
                cout<<" \nEnter your Birth Month: ";
                    cin >> bmonth;
                cout<<" \nEnter your Birth Day: ";
                    cin >> bday;
                cout<<" \nEnter your Birth Year: ";
                    cin >> byear;
                cout<<" \nEnter today's Year: ";
                    cin >> year;
                cout<<" \nEnter your Nationality: ";
                    cin >> nationality;
                    
                    fullname = fname +' '+ mname +' '+ lname;
                    age = year - byear;
                    
                                
                        cout<<"\n\nResults:";
                                
                    cout<<"\n\n Your Fullname is: " << fullname;
                    cout<<"\n Your Address is: " << country +' '+ prov +' '+ city;
                    cout<<"\n Your Age: " << age;
                    cout<<"\n Your Birthmonth is: " << bmonth;
                    cout<<"\n Your Birthday is: " << bday + byear;
                    cout<<"\n Our current year is: " << year;
                    cout<<"\n Your Nationality is: " << nationality;
                                
                                
                        cout<<"\n\n Moving to your Grades";
                                    
                    cout<<"\n\n Enter your first grade: ";
                        cin >> fgrade;
                    cout<<"\n\n Enter your second grade: ";
                        cin >> sgrade;
                                                
                                    ave = (fgrade + sgrade) / 2;
                            cout<<"\n\n Your Average Grade is: " << ave;
                                                
                                                
                        if(ave >= 95){
                        cout<<"\n\n You passed";
                        cout<<"\n Congrats";
                        cout<<"\n Your Grade letter is: A";
                                                        }
                        else if(ave >= 85){
                        cout<<"\n\n You passed";
                        cout<<"\n Pwede na";
                        cout<<"\n Your Grade letter is: B";
                                                        }
                        else if(ave >= 75){
                        cout<<"\n\n Pasang awa";
                        cout<<"\n Mag aral ka pa boi";
                        cout<<"\n Your Grade letter is: C";
                                                        }
                                                                        
                        cout<<"\n\nNow Simple Calculator";
                                                                        
                        cout<<"\n\nEnter Firstnumber: ";
                            cin>> num1;
                        cout<<"\nEnter Secondnumber: ";
                            cin>> num2;
                        cout<<"\nEnter the Operation: ";
                            cin>> op;
                                                                                
                                cout<<"\n\nRESULTS";
                                                                                
                        switch (op) 
                        {
                        case '+':;
                        sum = num1 + num2;
                        cout<<"\n\nThe sum of Num1 and Num2 is : "<< sum;
                                                                                                
                        break;
                            }
                        switch (op) 
                        {
                        case '-':;
                        sum = num1 - num2;
                        cout<<"\n\nThe Difference of Num1 and Num2 is : "<< dif;
                                                                                                
                        break;
                            }
                        switch (op) 
                        {
                        case '*':;
                        sum = num1 * num2;
                        cout<<"\n\nThe Product of Num1 and Num2 is : "<< prod;
                                                                                                
                        break;
                            }
                        switch (op) 
                        {
                        case '/':;
                        sum = num1 / num2;
                        cout<<"\n\nThe Quotient of Num1 and Num2 is : "<< quot;
                                                                                                
                        break;
                            }                 
                        return 0;
                        }