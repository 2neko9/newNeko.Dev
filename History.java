public class History extends Library {
    static String publisher = "SJNPS", size = "large", illustrator = "Mikee", description = "country history";
    static private String birthPlace = "Cabiao", authorBio = "Historian", birthDate = "June 18, 1975";
    static int datePub = 2022, totalPages = 280, weight = 190;
    private int price = 90;

    History(String author, String title){
        super("The History Author is: " + author,"The History Title is: " + title);
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
