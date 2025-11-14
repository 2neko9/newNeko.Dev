import java.util.Scanner;
public class quiz5_1{
     public static void main(String[] args) {
         Scanner obj = new Scanner(System.in);
         String fname, lname, year_level, course_abbr, name;
         System.out.print("Please enter your first name : ");
         fname = obj.nextLine();
         System.out.print("Please enter your lastname : ");
         lname = obj.nextLine();
         System.out.print("Please enter your year level : ");
         year_level = obj.nextLine();
         System.out.print("Please enter your course abbreviation : ");
         course_abbr = obj.nextLine();
         System.out.print("Please enter your grade point average : ");
         Double grade_point = obj.nextDouble();
         name = fname + " " + lname;
         System.out.println("\nYou have entered the following information : ");
         System.out.println("Name : " + name);
         System.out.println("Year Level : " + year_level);
         System.out.println("Course : " + course_abbr);
         System.out.println("Average Grade : " + grade_point);
     }
}