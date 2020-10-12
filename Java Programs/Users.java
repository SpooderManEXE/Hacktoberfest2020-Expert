
/**
 * Write a description of class Users here.
 *
 * @author(Tearz)
 * @version 
 */
public class Users
{
    /**instance variables*/
   private String username;
   private String userpassword;
   

/** constructor with 3 attributes in the parenthesis*/
public Users(String username,String userpassword,int telephone_no){
 this.username=username;
 this.userpassword=userpassword;

}
/**Get methods, used to return values assigned to the attributes*/
public String getusername(){
    return username;
}


public String getuserpassword(){
    return userpassword;
}

/** The display method, used to print values in the attributes*/
public void Display() {
System.out.println("You have been saved in Tearz Recipe System");
 System.out.println("*******************************************");
System.out.println("name :"+username);
System.out.println("password :"+userpassword);
System.out.println("*******************************************");

}
}


















/** Tearz on mode*/