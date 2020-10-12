

import java.util.*;
/**
 * Write a description of class Homepage here.
 *
 * @author (Tearz)
 * @version ()
 */
public class Home
{
    static Scanner obj = new Scanner(System.in);
    
    /**Homepage Menu*/
     public static void homepage()
     {
          System.out.println("***********************************************");   
          System.out.println("Press 1: For Administrator purposes");
          System.out.println("Press 2: For Farmer services");
          System.out.println("Press 3: To search details about the company");
          System.out.println("Press 4: Member of the public ");
          System.out.println("************************************************");
     }
     
     /**
      * display the administrator's home interface.
      */
     public static void printAdministratorpage()
     {
          System.out.println("***************************************");   
          System.out.println("Press 1: To add new Farmer");
          System.out.println("Press 2: Remove a farmer ");
          System.out.println("Press 3: Exit Admin menu");
          System.out.println("Press 4: print out all registered Farmers "); 
          System.out.println("***************************************");
     }
     
    
     
     /**
      * prints the menu of the application for user services.
      */
     public static void Userservices()
     {
          System.out.println("***************************************"); 
          System.out.println("Press 1: For Adding Animal");
          System.out.println("Press 2: To exit customer services");
          System.out.println("Press 3: Searching available recipes");           
          System.out.println("***************************************");
     }
     
        
     
}

    

