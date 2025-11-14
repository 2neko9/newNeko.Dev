public class Novel extends Library {
    static String publisher = "Flask.inc", size = "medium", illustrator = "Joe", description = "love story" ;
    static private String birthPlace = "Pampanga", authorBio = "Prof", birthDate = "May 27, 1990";
    static int datePub = 2020, totalPages = 190, weight = 150; 
    private int price = 120;

    Novel(String author, String title){
        super("The Novel Author is: " + author,"The Novel Title is: " + title);
    }
    public static void authDet(){
        System.out.println("The Author is a: " + getAuthorBio());
            System.out.println("The Author BirthPlace is in: " + getBirthPlace());
                System.out.println("The Author BirthDate is on: " + getBirthDate());
    }
    public static void pubDet(){
        System.out.println("Publisher: " + publisher);
            System.out.println("Date Published: " + datePub);
    }
    public static void bookDet(){
        System.out.println("Book Description: " + description);
            System.out.println("With a size: " + size);
                System.out.println("Book weight is: " + weight);
                    System.out.println("The book total pages: " + totalPages);
    }
    public String getAuthor() {
        return this.author;
    }
    public String getTitle(){
        return this.title;
    }
    public int getPrice(){
        return price;
    }
    public static String getBirthPlace(){
        return birthPlace;
    }
    public static String getAuthorBio(){
        return authorBio;
    }
    public static String getBirthDate(){
        return birthDate;
    }
}
