import java.util.*;

public class StringPermutations {
    private static List<String> al = new ArrayList<String>();
    public static void main(String[] args) {
        StringPermutations obj = new StringPermutations();
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char[] voc = str.toCharArray();
        Arrays.sort(voc);
        String s = new String(voc);
        obj.permutate(s,0,s.length()-1);
        Collections.sort(al);
        for(int i = 0 ; i < al.size() ; i++)
            System.out.println(al.get(i));
        //int fixed = 1;
        System.out.print(al.size());
    }
    public void permutate(String s, int l, int r){
        if(l==r) {
           // System.out.println(s);
            al.add(s);
        }
        else
        {
            for(int i = l ; i <= r; i++)
            {
                s = swap(s,l,i);
                permutate(s,l+1,r);
                s = swap(s,l,i);
            }
        }
    }

    public static String swap(String s, int l , int r)
    {
        char temp;
        char[] charArray = s.toCharArray();
        temp = charArray[l];
        charArray[l] = charArray[r];
        charArray[r] = temp;
        return String.valueOf(charArray);
    }


}
/**
 * ABC
 * ACB
 * BAC
 * BCA
 *
 * abcd
 * acbd
 */
