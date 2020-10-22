import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.util.ArrayList;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class RelativeSorting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int size_first = sc.nextInt();
            int size_Second = sc.nextInt();
            TreeMap<Integer, Integer> first = new TreeMap<>();
            ArrayList<Integer> second = new ArrayList<>();

            int num;
            for (int i = 0; i < size_first; i++) {
                num = sc.nextInt();
                if (first.containsKey(num)) {
                    first.put(num, first.get(num) + 1);
                } else {
                    first.put(num, 1);
                }

            }

            for (int j = 0; j < size_Second; j++) {
                num = sc.nextInt();
                if (first.containsKey(num)) {
                    for (int i = 0; i < first.get(num); i++) {
                        System.out.print(num + " ");
                    }
                    first.remove(num);
                }
            }
            //System.out.println("Remaining elements");
            for (Map.Entry<Integer, Integer> hm : first.entrySet()) {
                if (hm.getValue() != 0)
                    System.out.print(hm.getKey() + " ");
            }
            System.out.println();
        }
    }
}

