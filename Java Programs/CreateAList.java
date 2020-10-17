import java.util.*;

public class CreateAList{

     public static void main(String []args){
         List<String> list1 = List.of("Hello", "World", "!");
         List<String> list = new ArrayList<>();
         list.add("Hello");
         list.add("World!");
          
         System.out.println(Arrays.toString(list.toArray()));
         System.out.println(Arrays.toString(list1.toArray()));
     }
}
