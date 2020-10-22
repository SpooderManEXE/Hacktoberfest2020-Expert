//Octal to Decimal
import java.io.*;
import java.util.*;
class Result{
    public static int convertDecimalToOctal(int decimal)
    {
        int octalNumber = 0, i = 1;

        while (decimal != 0)
        {
            octalNumber += (decimal % 8) * i;
            decimal /= 8;
            i *= 10;
        }

        return octalNumber;
    }
    public static int convertOctalToDecimal(int octal)
    {
        int decimalNumber = 0, i = 0;

        while(octal != 0)
        {
            decimalNumber += (octal % 10) * Math.pow(8, i);
            ++i;
            octal/=10;
        }

        return decimalNumber;
    }

}

class Octal_to_Decimal{
        public static void main(String[] args) {
            int decimal;
             Scanner scan =new Scanner(System.in);
             System.out.printf("Enter a value");
             decimal=scan.nextInt();
            Result res = new Result();
            int octal = res.convertDecimalToOctal(decimal);
            System.out.printf("Octal value of %d is %d ", decimal, octal);
            int deci = res.convertOctalToDecimal(octal);
            System.out.printf("\n \nDecimal value of %d is %d ", octal, deci);
        }
}
