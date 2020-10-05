public class Perfect_number {
    public static void main(String[] args) {
        int _number = 28;
        if(checkPerfectNumberOrNot(_number))
        {
            System.out.println(_number+" is a perfect number");
        }
        else
        {
            System.out.println(_number+" is not a perfect number");
        }
    }
    public static boolean checkPerfectNumberOrNot(int _number)
    {
        int sum=0;
        for(int i=1;i<=_number/2;i++)
        {
        if(_number%i==0)
        {
            sum+=i;
        }    
        }
        if(sum==_number)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
