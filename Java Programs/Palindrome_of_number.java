public class Paliandrome_of_number {
    public static void main(String args[]) {
        
        int _number = 12121;
        System.out.println("Entered Number is: "+_number);

        if(checkPalindromeOrNot(_number)){
            System.out.println(_number + " is a Palindrome");
        }
        else
        {
            System.out.println(_number + " is not a Palindrome");    
        }

    }
    public static Boolean checkPalindromeOrNot(int _number) {
        int temp = _number;
        int reverse = 0;
        int digit;
        while(_number!=0)
        {
            digit = _number%10;
            reverse = reverse * 10 + digit;
            _number = _number/10;    
        }
        if(reverse == temp)
        {
            return true;
        }
        else
        {
            return false;
        }
    } 
}
