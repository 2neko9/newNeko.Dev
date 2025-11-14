import java.util.Scanner;
public class MainClass {
    public static void main(String[] args){
    
        
        int dir;
        boolean isRunning = true;

            Library L1 = new Library("My Name is: Neil Gerald P. Lapuz ", "Welcome to: Neil's Library");
            Novel C1 = new Novel("Clenn" , "RnJ");
            Biography C2 = new Biography("Alexis", "Steve");            
            History C3 = new History("Lyean", "USA");    
        
                System.out.println("\t\t\tNeil's Library");
                System.out.println("\nAbout me: :)");
                System.out.println("------------------------------");
                L1.printDetails();
            
            
                    L1.logInfo();

                    
                        while(isRunning){
                            System.out.println("\n\n");
                            L1.dir();
                            Scanner myObj1 = new Scanner(System.in);
                                System.out.println("------------------------------");
                                    System.out.println("Select a Number: ");
                            dir = myObj1.nextInt();
                

        switch (dir)
                {
            case 1:;
                if(dir == 1){
                    System.out.println("\n\nBOOKS :)");
                        System.out.println("------------------------------\n");
                    for (int i = 0; i < L1.Cat.length; i++) {
                        System.out.println(L1.Cat[i]);
                    }
                    
                    System.out.println("\n");
                    C1.printDetails();
                    C2.printDetails();
                    C3.printDetails();

                    L1.order();
                    if (L1.money == false){
                        System.out.println("\n\n\t\t\tTHANK YOU!!!! " + Library.getName() + " COME AGAIN!!! <3\n\n");
                            isRunning = false;
                                break;
                    }
                break;
                }

            case 2:;
                System.out.println("\n\n\t\t\tTHANK YOU!!!! " + Library.getName() + " COME AGAIN!!! <3\n\n");
                isRunning = false;
                break;
                    
            }
            }
    }
}