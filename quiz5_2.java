import java.util.Scanner;
public class quiz5_2{
    public static void main(String[] args){
    Scanner obj = new Scanner(System.in);

    int size, total, order;

    System.out.println("Welcome to the Sandwich Corral");
    System.out.println("\nYou will be given choices for making your sandwich");
    System.out.println("Please enter your selection after each prompt and then press the key.");
    System.out.print("\nPlease enter you sandwich choice [ Ham, Beef, Cheese, Egg, Tuna] : ");
    String sandwich = obj.nextLine();
    System.out.print("Please enter you bread selection [ Wheat, White, Rye, Sourdough] : ");
    String bread = obj.nextLine();
    System.out.print("Please enter your choice of condiment [ Mayo, Mustard, Ketchup, none] : ");
    String condiment = obj.nextLine();
    System.out.print("Please enter your drink  choice [ Coke, Tea, Coffee, Water] : ");
    String drink = obj.nextLine();

    System.out.print("Please enter 25 for a half sandwich or 50 for a whole sandwich: ");
    size = obj.nextInt();
    System.out.print("\nHow many orders of Sandwich do you like? ");
    order = obj.nextInt();

    System.out.println("\nYou have entered the following inforation: \n");
    System.out.println("Sandwich : " + sandwich);
    System.out.println("Bread    : " + bread);
    System.out.println("Condiment: " + condiment);
    System.out.println("Drink    : " + drink);

    total = order * size + 20;
    System.out.println("\nTotal Bill : " + total);


    }
}