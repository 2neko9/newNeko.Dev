public class Biography extends Library {
    static String publisher = "SNA media", size = "small", illustrator = "Loyd", description = "life story" ;
    static private String birthPlace = "La Union", authorBio = "Student", birthDate = "December 20, 2000";
    static int datePub = 2018, totalPages = 30, weight = 130;
    private int price = 100;

    Biography(String author, String title){
        super("The Biography Author is: " + author,"The Biography Title is: " + title);
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
    public String getAuthor(){
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
