
// Java program for checking Internet connectivity 
import java.util.*; 
import java.io.*; 
import java.net.URL; 
import java.net.URLConnection; 
  
class checking_internet_connectivity { 
    public static void main(String args[]) 
    { 
        try { 
            URL url = new URL("https://www.google.com"); 
            URLConnection connection = url.openConnection(); 
            connection.connect(); 
  
            System.out.println("Connection Successful"); 
        } 
        catch (Exception e) { 
            System.out.println("Internet Not Connected"); 
        } 
    } 
} 
