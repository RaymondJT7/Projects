/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


/**
 *
 * @author Raymond James Tilstone
 */
// Importing all classes from the java.util package to use the Scanner class and the ArrayList class
import java.util.*;
public class BirthdayReminderArrayList {
    // Main class
    public static void main(String[] args){
        // Variable declaration and intialization
        String names;
        String birthdays;
        String searchName;
        int count = 0;
        final int MAX = 10;
        final String SENTINEL = "ZZZ";
        Scanner userInput = new Scanner(System.in);
        
        // Creating instances of the ArrayList class
        ArrayList arrListName = new ArrayList();
        ArrayList arrListBirthday = new ArrayList();
        
        // Interating a fixed number of times to keep asking for user input until the sentinel value is entered
        for(int x = 0; x <= MAX; x++){
            // Prompting the user to enter names
            System.out.println("Enter a name (or enter zzz to stop entering names): ");
            // Using the Scanner class to get the user input
            names = userInput.nextLine();
            
            // Checking if the sentinel value is entered and then exits the loop
            if(names.equalsIgnoreCase(SENTINEL)){
                break;
            }
            
            // Populating the arrListName ArrayList with the names entered by the user
            arrListName.add(names);
            // Prompting the user to enter the birthdates for the previously entered name
            System.out.println("Enter the birthdate for " + arrListName.get(x) + ": ");
            // Using the Scanner class to get the user input
            birthdays = userInput.nextLine();
            // Populating the arrListBirthdays ArrayList with the birthdates entered by the user
            arrListBirthday.add(birthdays);
            // Incrementing the count variable to keep track of how many names are entered
            count++;
            
        }
        // Outputting the total number of names entered
        System.out.println("\nThe total number of names entered is: " + count);
        // Names header
        System.out.println("\nThe entered names are: ");
        
        // Iterating through the arrListName ArrayList to display all of the names entered
        for(int x = 0; x < arrListName.size(); x++){
            System.out.println(x + 1 + ": " + arrListName.get(x));
        }
        
        while(true){
            // Continuously asking the user the enter a name to get their birthday until sentinel value is entered
            System.out.println("\nEnter a name to get their birthday (or enter zzz to exit): ");
            // Storing the userInput from the Scanner inside a String
            searchName = userInput.nextLine();
            
            // Checking if the sentinel value is entered and then exits the loop
            if(searchName.equalsIgnoreCase(SENTINEL)){
                break;
            }
            
            // Iterating through the ArrayList to check if the name entered by the user is found in the list
            for(int x = 0; x < arrListName.size(); x++){
                if(searchName.equalsIgnoreCase((String)arrListName.get(x))){
                    // If the name is found the birthdate for that user will be outputted to the console
                    System.out.println("\nThe birthdate for " + arrListName.get(x) + " is: " + arrListBirthday.get(x));
                    // If the name is not found an error message will display in the console
                }else if(searchName.equalsIgnoreCase((String)arrListName.get(x))){
                    System.out.println("An invalid name was entered.");
                }
            }
        }
    }   
}
