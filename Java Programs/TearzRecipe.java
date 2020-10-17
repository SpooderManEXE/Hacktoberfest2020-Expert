 
import java.util.*;

/**
 * Write a description of class TearzRecipe here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TearzRecipe
{
    static String loginAs = "unknown";
    static ArrayList<Users>           user = new ArrayList<>();
      static Scanner scan = new Scanner(System.in);
    public static void main ( String [] recipe ){
    runHome();
    }
    
    
    static public void login(){

        System.out.println("* * * * * * * * * * * * * * *****");
        System.out.println("Tearz Recipe");
        System.out.println("* * * * * * * * * * * * * * *****");

        System.out.println("Enter your name: ");
        String name = scan.next();

        System.out.println("Enter you password: ");
        String password = scan.next(); 

        if(!(user.size() == 0))
        {
            for(int i =0; i < user.size(); i++)
            {
                Users currentUser = user.get(i);
                
                String currentName = currentUser.getusername();
                
                String currentID = currentUser.getuserpassword();
                
                if(name.equals(currentName) && password.equals(currentID))
                {
                    loginAs =currentName;
                    System.out.println("Welcome " + name + ", you now have access to Tearz Recipe system.");
                    Home.Userservices();
                }
                else{System.out.println("User not registered Kgano"); runHome();} 
            }
        }
        else{System.out.println("No such User in the system,please go for registration, and i dont want to repeat thz go now"); runHome();}
    }
    
       public static void runHome(){ 
        
        Scanner obj = new Scanner(System.in);

        Home.homepage();

        String inString = obj.next();

        int number = Integer.parseInt(inString);

        switch(number)
        {  

            case 1:  
           
            Home.printAdministratorpage();
            inString = obj.next();
            number = Integer.parseInt(inString);
            switch(number) {

                

                case 1: String space = obj.nextLine();//move scanner object to the nextline...

                System.out.println("Enter the customer's fullname");
                String userName = obj.next();

                System.out.println("Input customer's contact details");
                int usercontact = obj.nextInt();

                System.out.println(" Enter your account password");
                String userpassword = obj.next();

                Users newuser = new Users(userName, userpassword,usercontact);
                
                if(user.size() == 0)
                {
                    user.add(newuser); 
                    System.out.println("The user has been added successfully."); 
                    runHome();
                }

                else
                {
                    boolean registered=false;
                    for(int i = 0; i < user.size(); i++)
                    { 
                        Users element = user.get(i);  
                        String currentName =  element.getusername();
                        String currentID = element.getuserpassword();

                        
                        if(userName.equals(currentName) && userpassword.equals(currentID))
                        {  
                            System.out.println("The User already exists.");
                            registered=true;
                            break;
                        }
                    }
                    if(registered==false)
                    {
                        user.add(newuser);
                        
                        System.out.println("The User has been added successfully.");

                        runHome();
                        
                        break;
                    }
                }
            }
        break;
          case 2:
            /**
             * User services menu
             */     login();
            String instring = obj.next();
            int numbers = Integer.parseInt(instring);}
    }
}
    



