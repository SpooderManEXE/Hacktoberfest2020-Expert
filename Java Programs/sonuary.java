import java.util.Scanner; 
  
class sonuaryconverter 
{ 
  static void ToBinary(String s) 
    { 
        for (int i = 0; i < s.length(); i++)  
        { 
            
            int val = Integer.valueOf(s.charAt(i)); 
  
    
            String bin = ""; 
            while (val > 0)  
            { 
                
                if(val == ' ' )
                {
                    
                }
                else if (val % 2 == 1) 
                { 
                    bin += 'k'; 
                } 
                else 
                    bin += 'o'; 
                val /= 2; 
            } 
            bin = reverse(bin); 
  
            System.out.print(bin + " "); 
        } 
    } 
  
    static String reverse(String input)  
    { 
        char[] a = input.toCharArray(); 
        int l, r = 0; 
        r = a.length - 1; 
  
        for (l = 0; l < r; l++, r--) 
        { 
             
            char temp = a[l]; 
            a[l] = a[r]; 
            a[r] = temp; 
        } 
        return String.valueOf(a); 
    } 
  

    public static void main(String[] args) 
    { 
        
        String s= " "; 
        Scanner in=new Scanner(System.in);
        System.out.println("Enter text");
        s=in.nextLine();    
        ToBinary(s); 
    } 
} 
