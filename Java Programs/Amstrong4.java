public class Amstrong {
    public static void main(String[] args) {
        int _number = 1634;
        if(isAmstrong(_number)){
            System.out.println(_number+" is a Amstrong Number");
        }
        else{
            System.out.println(_number+" is not a Amstrong Number");
        }
    }
    public static boolean isAmstrong(int _number)
    {
        int digits=0;
        int temp=_number;
        int rem,sum = 0;
        while(temp!=0)
        {
            digits++;
            temp = temp/10;

        }
        temp = _number;
        while(temp!=0)
        {
               rem = temp % 10;
               sum = sum + power(rem,digits);
               temp = temp / 10;
        }
        if(_number == sum)
        {
            return true;
        }
        else
        {
            return false;
        }

    }
    public static int power(int rem,int digits)
    {
        int i,p=1;
        for(i=1;i<=digits;i++)
        {
            p = p*rem;
        }
        return p;
    }
}
