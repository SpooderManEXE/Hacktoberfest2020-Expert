public class Reverse_of_number {
    public static void main(String args[]) {
        int _number = 894;
        System.out.println("Entered Number is: "+_number);
        System.out.println("Reversed Number is: " + reversedNumber(_number));

    }
    public static int reversedNumber(int _number){
        int reversed = 0;
        while(_number!=0)
        {
            int digit = _number % 10;
            reversed = reversed * 10 + digit;
            _number /= 10;
         }
        return reversed;
    }
}

