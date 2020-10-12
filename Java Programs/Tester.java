import java.io.*;
import java.util.Scanner;
/**
 * Write a description of class Tester here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Tester
{
    static Rabbit [] rabbit = new Rabbit[10];
    public static void main(String [] args) throws IOException{

        File file = new File("rabbits.txt");
        Scanner scan =new Scanner(file);

        int i =0;

        while(scan.hasNext()){

            String[] splits=scan.nextLine().split(" ");

            Rabbit rbt =new Rabbit(splits[0],Double.parseDouble(splits[1]));

            rabbit[i] =rbt;
            i++;
        }
        sortRabbits(rabbit);
        Display();

    }

    /**
     * Method sortRabbits: accept an array of Rabbit objects and 
     * sort it using bubble sort according to ascending order 
     * of weight.
     */
    public static void sortRabbits (Rabbit [] rabbit){

        int n = rabbit.length;  
        Rabbit temp ;  
        for(int i=0; i < n; i++){  
            
            for(int j=1; j < (n-i); j++){  
                
                if(rabbit[j-1].getweight() > rabbit[j].getweight()){  

                    temp = rabbit[j-1];  
                    rabbit[j-1] = rabbit[j];  
                    rabbit[j] = temp;  
                }  

            }  
        } 
    }

    /**
     *Method isOverweight – this method should accept Rabbit object
     *and return true when the Rabbit’s weight exceeds 2kg and 
     *false otherwise.
     */
    public boolean isOverweight(Rabbit  rabbits){
        
        for(Rabbit rbt : rabbit){
            if(rbt.getweight() > 2){ 
            return true;}
          
        }
        
       return false;
    }

    /**
     * Display Rabbit objects on the monitor, one per line.
     * Lastly, send information about all overweight rabbits to
     * overweight.txt.
     */
    public static void Display() throws IOException{
        for(Rabbit rbt : rabbit){
            System.out.println(rbt);
        }

        File files = new File("overweight.txt");
        PrintWriter pw = new PrintWriter(files);

        for(Rabbit rabt : rabbit){
            if(rabt.getweight() > 2){
                pw.println(rabt);
            }
        } pw.close();

    }

    
    
}
