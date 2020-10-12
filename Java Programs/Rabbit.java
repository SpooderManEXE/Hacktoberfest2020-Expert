
/**
 * Write a description of class Rabbit here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Rabbit
{
    /**
    * Instance variable
    */
    private String name;
    private double weight;
    /**
     * constructors of class Rabbit
     */
    public Rabbit(){}
    
    public Rabbit(String name, double weight){
    
    this.name= name;
    this.weight = weight;
    }
    /**
     * Mutator and Accessor methods
     */
    public String getName(){
    return name;
    }
    
    public double getweight(){
    return weight;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setweight(double weight) {
	this.weight = weight;
}
    
    
   
    public String toString(){
       return "name:"+name+"\t\t"+"weight:"+weight+" Kg"; 
    }
}
