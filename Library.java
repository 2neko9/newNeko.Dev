import java.util.Scanner;
public class Library {
    String author, title, conNum, name2;
    static String name;
    int cat, age, numBooks, x, i, k;
    double sub1, sub2, sub3, total, change, balance = 0, cash;
    boolean wCash = true, money = true;
    
    
    String [] Home = {"1. Books :: 2. Exit"};
    double [] price = {0,120,90, 100 };
    String [] Cat = {"", "1. Novel = 120.00php ", "2. History = 90.00php ", "3. Biography = 100.00php"};
    String [] Cat2 = {"", " Novel = 120.00php ", " History = 90.00php ", " Biography = 100.00php"};
    
    Library (String author, String title){
        this.author = author;
        this.title = title;
    }

    public void logInfo(){
        System.out.println("\n\nNOTE: ALL BOOKS MUST BE RETURNED WITHIN 7DAYS AND YOU WILL BE CONTACTED USING YOUR INFO.: :)");
            System.out.println("\nPlease Log in: :)");
                System.out.println("------------------------------");

        Scanner myObj3 = new Scanner(System.in);  // Create a Scanner object
            System.out.println("Enter your Name: ");
                name = myObj3.nextLine(); 
        
        
        Scanner myObj4 = new Scanner(System.in);  // Create a Scanner object
            System.out.println("Enter your Age: ");
                age = myObj4.nextInt();

        if (age >= 18){
            Scanner oc = new Scanner(System.in);
                System.out.println("Enter your Contact Number: ");
                    conNum = oc.nextLine();
    
            System.out.println("\n\nYour info: :) Hello " + name);
                System.out.println("------------------------------");
            
            System.out.println("Your Name is: " + name);
                System.out.println("Your Age is: " + age );
                    System.out.println("Your Contact Number is: " + conNum + "\n"); 

            } else if(age < 18){
                Scanner gur = new Scanner(System.in);  // Create a Scanner object
                    System.out.println("Enter your Parent/Guardian's Name: ");
                        name2 = gur.nextLine(); 

                Scanner oc = new Scanner(System.in);
                    System.out.println("Enter your Parent/Guardian's Contact Number: ");
                        conNum = oc.nextLine();
        
                System.out.println("\n\nYour info: :) Hello " + name);
                    System.out.println("------------------------------");
                
                System.out.println("Your Name is: " + name);
                    System.out.println("Your Age is: " + age );
                        System.out.println("Your Parent/Guardian's Name is: " + name2);
                            System.out.println("Your Parent/Guardian's Contact Number is: " + conNum + "\n"); 
            }
    

        }

        
        public static String getName(){
            return name;
        }
        
        public void dir(){

            for (int i = 0; i < Home.length; i++) {
                System.out.println(Home[i]);
            }
        }

        public void order(){
            
            Scanner scanner = new Scanner(System.in);
                System.out.print("\n\nHow many Books do you want to rent: :)");
                System.out.println("\n--------------------------------------");
                    int x = scanner.nextInt();
        
            if (x > 3) {
                System.out.println("\nThe Order Limit is 3!!!");
                    return;
            }
        
        int[] myArray = new int[x];
        int[] myArray2 = new int[x];

        
        for (int i = 0; i < x; i++) {
            System.out.print("\n\nWhat Book Do You Want to Rent: " + (i + 1) + ": ");
                myArray[i] = scanner.nextInt();

            System.out.print("How Many of This Book you Want to Rent: ");
                myArray2[i] = scanner.nextInt();

            
            System.out.println("\n------------------------------");
                System.out.println("This is the Book you Chose: " + myArray[i] );
            if (myArray[i] == 1) {
                System.out.println("Novel Book: :)");
                    System.out.println("------------------------------");
                        System.out.println("\t\t::Book Details::\n");
                    Novel.authDet();
                    Novel.pubDet();
                    Novel.bookDet();
            } if (myArray[i] == 2){
                System.out.println("History Book: :)");
                    System.out.println("------------------------------");
                        System.out.println("\t\t::Book Details::\n");
                    History.authDet();
                    History.pubDet();
                    History.bookDet();
            } if (myArray[i] == 3){
                System.out.println("Biography Book: :)");
                    System.out.println("------------------------------");
                        System.out.println("\t\t::Book Details::\n");
                    Biography.authDet();
                    Biography.pubDet();
                    Biography.bookDet();
            }
        }
                        
                    System.out.println("\n\n\t\t\tYour Book Orders:\n\n");
        
                    System.out.println("Your Balance is: " + balance + "\n");

        for (int i = 0; i < x; i++) {
            if (myArray[i] <= 3) {
                    System.out.println("Book #" + (i + 1) + ": " + Cat2[myArray[i]] + " X " + myArray2[i] + " = " + (myArray2[i] * price[myArray[i]]));
            } else if (myArray[i] > 3) {
                    System.out.println("The Book isn't on the Catalogue.");
            } else if (myArray[i] < 1) {
                    System.out.println("The Book isn't on the Catalogue.");
            }
            }

        for (int i = 0; i < x; i++) {
            if(myArray[i] == 1){
                sub1 += 120.00 * myArray2[i];
            } else if(myArray[i] == 2){
                sub2 += 90.00 * myArray2[i];
            } else if(myArray[i] == 3){
                sub3 += 100.00 * myArray2[i];
            }
                        
            total = sub1 + sub2 + sub3;
        }
            System.out.println("\nThe Total amount is: " + "Php " + total);
            Cashout();
                }
                    
            
public void Cashout(){
            while(wCash){
                Scanner myObj7 = new Scanner(System.in);
                    System.out.println("\nEnter your Cash: ");
                    System.out.println("------------------------------");
                        cash = myObj7.nextInt();
                System.out.println("Your Cash Amount is: " + cash +"php");
            break;
            }
            
            change = cash - total;
            balance = change;
            
            
            while(money){
                if(cash < total){
                    System.out.println("\n------------------------------");
                    System.out.println("You don't have enough Money!!!\n\n");
                    money = false;
                
                } else if( cash >= total){
                    System.out.println("\n------------------------------");
                    System.out.println("Your Change is: Php " + change);
                    System.out.println("Your New Balance is: " + balance);
            }
            break;
        }
                
                sub1 = 0;
                sub2 = 0;
                sub3 = 0;
                cash = balance;
                wCash = false;
                }
        
        public void printDetails(){
            System.out.println(this.author);
            System.out.println(this.title + "\n");
        }
}
