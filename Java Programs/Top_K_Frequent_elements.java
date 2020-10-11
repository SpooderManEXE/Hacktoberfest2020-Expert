import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Top_K_Frequent_elements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {3,3,3,3,6,6,6,7,7,9};
        int max_frequency = 2;

        //#1 : build frequencies using HMAP
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int x : arr)
        {
            hm.put(x,hm.getOrDefault(x,0)+1);
        }

        //#2: sort by frequencies
        PriorityQueue<Integer> pq = new PriorityQueue<>((x,y) -> (hm.get(x)-hm.get(y)));
        System.out.println(hm);
        for(int x : hm.keySet())
        {
            System.out.println(x);
            pq.add(x);
            if(pq.size()>max_frequency)
                pq.poll();
        }
        System.out.println(pq);
    }
}

