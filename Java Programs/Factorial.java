public class Factorial {
    public static void main(String[] args) throws Exception {
        int _number = 5;
        System.out.println("The Factorial of "+_number+" is: "+fact(_number));

    }
    public static int fact(int _number){
        int fact = 1 ;
        for(int i=1;i<=_number;i++)
        {
            fact = fact * i;
        }
        return fact;
    }
}
